import os
import shutil

# Folder to organize
path = r"test_folder" #Enter Path here

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar"]
}

# Count moved files
count = 0

# Read all files in folder
files = os.listdir(path)

for file in files:

    source_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(source_path):
        continue

    # Get extension
    _, extension = os.path.splitext(file)
    extension = extension.lower()

    destination_folder = "Others"

    # Find category
    for folder, extensions in categories.items():
        if extension in extensions:
            destination_folder = folder
            break

    # Create folder if not exists
    destination_path = os.path.join(path, destination_folder)

    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    # Move file
    shutil.move(
        source_path,
        os.path.join(destination_path, file)
    )

    print(f"Moved: {file} -> {destination_folder}")
    count += 1

print("\nOrganization Complete!")
print(f"Total Files Moved: {count}")