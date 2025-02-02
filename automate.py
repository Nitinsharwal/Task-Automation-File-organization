import os
import shutil

# Input target directory
filePath = input('Enter path of the directory to organize: ')
TARGET_DIR = os.path.expanduser(filePath)

# File categories for organizing
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Others": []
}

# Create folders based on categories
def create_folders(base_dir):
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

# Handle duplicate file names
def move_with_overwrite(src, dest):
    if os.path.exists(dest):
        base, ext = os.path.splitext(dest)
        counter = 1
        while os.path.exists(dest):  # Append a counter to avoid overwriting
            dest = f"{base}_{counter}{ext}"
            counter += 1
    shutil.move(src, dest)

# Organize files efficiently
def organize_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        # Skip organizing the already created category folders
        if root == base_dir:
            dirs[:] = [d for d in dirs if d not in FILE_CATEGORIES.keys()]

        for item in files:
            item_path = os.path.join(root, item)
            _, ext = os.path.splitext(item)
            ext = ext.lower()

            # Determine destination folder
            destination = "Others"
            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    destination = category
                    break

            # Move file to the destination folder
            dest_folder = os.path.join(base_dir, destination)
            dest_path = os.path.join(dest_folder, item)
            try:
                move_with_overwrite(item_path, dest_path)
                print(f"Moved: {item} -> {dest_folder}")
            except shutil.Error as e:
                print(f"Error moving {item}: {e}")

def main():
    if not os.path.exists(TARGET_DIR):
        print("The specified directory does not exist. Please check the path and try again.")
        return

    create_folders(TARGET_DIR)
    organize_files(TARGET_DIR)
    print("File organization complete!")

if __name__ == "__main__":
    main()
