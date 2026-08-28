import os
import shutil
from datetime import datetime

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"]
}

LOG_FILE_NAME = "organizer_log.txt"


def organize_directory():
    path = input("\nEnter folder path to organize:\n> ").strip()

    if not os.path.exists(path):
        print("Error: The specified path does not exist.")
        return
    if not os.path.isdir(path):
        print("Error: The path is not a directory.")
        return

    print("\nOrganizing files...\n")
    moved_count = 0
    skipped_dir_count = 0
    log_file_path = os.path.join(path, LOG_FILE_NAME)

    with open(log_file_path, "a", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n--- Execution Run: {timestamp} ---\n")

        for item in os.listdir(path):
            if item == LOG_FILE_NAME:
                continue

            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                skipped_dir_count += 1
                continue

            _, ext = os.path.splitext(item)
            ext = ext.lower()

            target_category = "Others"
            for category, extensions in CATEGORIES.items():
                if ext in extensions:
                    target_category = category
                    break

            dest_dir = os.path.join(path, target_category)
            os.makedirs(dest_dir, exist_ok=True)

            dest_path = os.path.join(dest_dir, item)
            shutil.move(full_path, dest_path)

            log_entry = f"[MOVED] {item} -> {target_category}/"
            print(log_entry)
            log_file.write(log_entry + "\n")
            moved_count += 1

        summary_line = f"Summary: {moved_count} Files Moved, {skipped_dir_count} Subdirectories Skipped\n"
        print(f"\n{summary_line.strip()}")
        log_file.write(summary_line)


def read_logs():
    path = input("\nEnter folder path to view logs:\n> ").strip()

    if not os.path.exists(path) or not os.path.isdir(path):
        print("Error: Invalid directory path.")
        return

    log_file_path = os.path.join(path, LOG_FILE_NAME)

    if not os.path.exists(log_file_path):
        print(f"\nNo previous log file ('{LOG_FILE_NAME}') found in this directory.")
        return

    print(f"\n================ LOG HISTORY ================")
    # Open log file in read mode ("r") using context manager
    with open(log_file_path, "r", encoding="utf-8") as log_file:
        content = log_file.read()
        if content.strip():
            print(content)
        else:
            print("[Log file is empty]")
    print("=============================================")


def main():
    print("============================================")
    print("             FILE ORGANIZER v4.0            ")
    print("============================================\n")
    print("1. Organize Directory")
    print("2. View Log History")

    choice = input("\nSelect an option (1 or 2):\n> ").strip()

    if choice == "1":
        organize_directory()
    elif choice == "2":
        read_logs()
    else:
        print("Invalid choice. Please run the script again and select 1 or 2.")


if __name__ == "__main__":
    main()