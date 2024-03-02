import re

def find_latest_version(S):
    if not S:  # Check for empty array
        return -1

    latest_version = -1
    pattern = r"File_(\d+)"
    
    for filename in S:
        match = re.match(pattern, filename)
        if match:
            version = int(match.group(1))
            latest_version = max(latest_version, version)

    return latest_version





