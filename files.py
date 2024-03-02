def find_latest_version(files, size):
    if not files:
        return -1

    latest_version = 0
    latest_file = ""

    for file in files:
        if file.startswith("File_"):
            version_str = file[5:]
            if version_str.isdigit():
                version = int(version_str)
                if version > latest_version:
                    latest_version = version
                    latest_file = file

    return latest_file if latest_file else -1

# Example usage with an empty array
input1_empty = []
input2_empty = 0
output_empty = find_latest_version(input1_empty, input2_empty)
print(output_empty)
