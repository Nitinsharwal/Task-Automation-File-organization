import os
import shutil

filePath = input('Enter path of file : ')
TARGET_DIR = os.path.expanduser(filePath)
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp",".wbep"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Others": []
}

def create_folders(base_dir):
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

def organize_files(base_dir):
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path):
            continue
        
        _, ext = os.path.splitext(item)
        ext = ext.lower()
        destination = "Others"  
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                destination = category
                break
        
        dest_folder = os.path.join(base_dir, destination)
        shutil.move(item_path, dest_folder)
        print(f"Moved: {item} -> {dest_folder}")

def main():
    create_folders(TARGET_DIR)
    organize_files(TARGET_DIR)
    print("File organization complete!")

if __name__ == "__main__":
    main()
