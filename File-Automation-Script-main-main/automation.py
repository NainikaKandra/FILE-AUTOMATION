import os
import shutil
import logging


logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
}



def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"



def sort_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            return

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            
            if os.path.isdir(file_path):
                continue

            _, ext = os.path.splitext(file_name)
            category = get_category(ext)

            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)

            new_path = os.path.join(category_folder, file_name)
            shutil.move(file_path, new_path)

            logging.info(f"Moved file: {file_name} -> {category}/")
            print(f"Moved: {file_name} -> {category}/")

    except Exception as e:
        logging.error(f"Error while sorting files: {e}")
        print("An error occurred while sorting files.")



def rename_files(folder_path, prefix):
    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            return

        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        if not files:
            print("No files found to rename.")
            return

        for index, file_name in enumerate(files, start=1):
            old_path = os.path.join(folder_path, file_name)
            _, ext = os.path.splitext(file_name)
            new_name = f"{prefix}_{index}{ext}"
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)

            logging.info(f"Renamed file: {file_name} -> {new_name}")
            print(f"Renamed: {file_name} -> {new_name}")

    except Exception as e:
        logging.error(f"Error while renaming files: {e}")
        print("An error occurred while renaming files.")



def delete_empty_folders(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            return

        deleted_any = False

        for root, dirs, files in os.walk(folder_path, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if not os.listdir(dir_path):  # folder is empty
                    os.rmdir(dir_path)
                    logging.info(f"Deleted empty folder: {dir_path}")
                    print(f"Deleted empty folder: {dir_path}")
                    deleted_any = True

        if not deleted_any:
            print("No empty folders found.")

    except Exception as e:
        logging.error(f"Error while deleting empty folders: {e}")
        print("An error occurred while deleting empty folders.")



def main():
    while True:
        print("\n===== FILE AUTOMATION MENU =====")
        print("1. Sort files into folders by type")
        print("2. Rename files in a folder")
        print("3. Delete empty folders")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            folder = input("Enter folder path to sort files: ").strip()
            sort_files(folder)

        elif choice == "2":
            folder = input("Enter folder path to rename files: ").strip()
            prefix = input("Enter prefix for renamed files: ").strip()
            rename_files(folder, prefix)

        elif choice == "3":
            folder = input("Enter folder path to clean empty folders: ").strip()
            delete_empty_folders(folder)

        elif choice == "4":
            print("Exiting program.")
            logging.info("Program exited by user.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()