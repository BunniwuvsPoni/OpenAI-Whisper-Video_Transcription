# Date last updated: 2024/11/17

# This function is intended to: Select a Directory from the local system
def select_directory():
    import sys
    import tkinter
    from tkinter import filedialog

    root = tkinter.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory()

    if not folder_path:
        sys.exit ("Error: Null or empty directory. Exiting application...")
    else:
        print (folder_path)

    return folder_path

# This function is intended to: Filter files in a specified directory
def filter_directory(directory, filter):
    import os
    import sys

    # List to store filtered files
    filteredFiles = []

    # Iterate through the directory
    for file_name in os.listdir(directory):
        # Check if the file matches filter
        if file_name.endswith(filter):
            filteredFiles.append(file_name)

    if not filteredFiles:
        sys.exit ("Error: No files found matching filter in directory. Exiting application...")
    else:
        print(filteredFiles)

    return filteredFiles