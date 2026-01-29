import os
import subprocess
import re
from pathlib import Path

def get_git_hash(file_path):
    """Gets the latest commit hash for a specific file."""
    try:
        # Use git log to get the latest commit hash for the file
        result = subprocess.run(
            ['git', 'log', '-n', '1', '--pretty=format:%H', '--', str(file_path)],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def parse_sync_metadata(file_path):
    """Parses .rst file for :sync_target: and :sync_hash: in comments."""
    sync_target = None
    sync_hash = None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        # Read the first few lines to find metadata block
        # Look for comment block at the start
        content = f.read(1024) # Read first 1KB should be enough
        
        target_match = re.search(r':sync_target:\s+(.+)', content)
        hash_match = re.search(r':sync_hash:\s+([a-f0-9]+)', content)
        
        if target_match:
            sync_target = target_match.group(1).strip()
        if hash_match:
            sync_hash = hash_match.group(1).strip()
            
    return sync_target, sync_hash

def check_sync():
    root_dir = Path("docs")
    out_of_sync_count = 0
    
    print(f"{'File':<60} | {'Status':<15} | {'Source Change'}")
    print("-" * 100)

    for rst_file in root_dir.rglob("*.rst"):
        target_rel_path, recorded_hash = parse_sync_metadata(rst_file)
        
        if target_rel_path and recorded_hash:
            # Resolve absolute path of the target
            # sync_target is relative to the rst_file location
            target_abs_path = (rst_file.parent / target_rel_path).resolve()
            
            # Check if target file exists
            if not target_abs_path.exists():
                print(f"{str(rst_file):<60} | {'ERROR':<15} | Target not found: {target_rel_path}")
                continue

            current_hash = get_git_hash(target_abs_path)
            
            if not current_hash:
                 print(f"{str(rst_file):<60} | {'ERROR':<15} | Not tracked by git: {target_rel_path}")
                 continue

            if current_hash != recorded_hash:
                out_of_sync_count += 1
                print(f"{str(rst_file):<60} | {'OUTDATED':<15} | {recorded_hash[:7]} -> {current_hash[:7]}")
                print(f"  Command to view diff: \n  git diff {recorded_hash} {current_hash} -- {target_abs_path}\n")
            else:
                # Optional: Verbose mode could show synced files
                # print(f"{str(rst_file):<60} | {'SYNCED':<15} |")
                pass

    if out_of_sync_count == 0:
        print("\nAll files are in sync!")
    else:
        print(f"""\nFound {out_of_sync_count} outdated file(s). Please
    1. find the updates with the `git diff` command provided
    2. update the files
    3. write the git commit hash of the sync_target back to sync_hash
""")

if __name__ == "__main__":
    check_sync()
