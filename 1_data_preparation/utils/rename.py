import os
import sys


def rename_files(folder_path, file_type):
    # Get all files and Sort files
    file_list = [file for file in os.listdir(folder_path) if file.endswith(file_type)]
    file_list.sort()

    # Rename files
    for index, file_name in enumerate(file_list):
        # New file name
        new_file_name = f"{index + 1}.{file_type}"  #

        # Full path
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename file
        os.rename(old_file_path, new_file_path)


def main():
    if len(sys.argv) != 3:
        print("Please specify folder path and file type.")
        sys.exit(1)
    folder_path, file_type = sys.argv[1:]
    rename_files(folder_path, file_type)

main()
