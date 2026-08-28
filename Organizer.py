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

print("============================================")
print("             FILE ORGANIZER v3.0            ")
print("============================================\n")

path = input("Enter folder path:\n> ").strip()

if not os.path.exists(path):
    print("Error: The specified path does not exist.")
elif not os.path.isdir(path):
    print("Error: The path is not a directory.")
else:
    print("\nOrganizing files...\n")
    moved_count = 0
    skipped_dir_count = 0

    log_file_path = os.path.join(path, LOG_FILE_NAME)

    # Open log file in append mode ("a") using a context manager
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n--- Execution Run: {timestamp} ---\n")

        for item in os.listdir(path):
            # Skip the log file itself so it isn't moved into "Others/"
            if item == LOG_FILE_NAME:
                continue

            full_path = os.path.join(path, item)

            # Skip subdirectories
            if os.path.isdir(full_path):
                skipped_dir_count += 1
                continue

            # Extract extension and normalize
            _, ext = os.path.splitext(item)
            ext = ext.lower()

            # Identify target folder category
            target_category = "Others"
            for category, extensions in CATEGORIES.items():
                if ext in extensions:
                    target_category = category
                    break

            # Create target folder if missing
            dest_dir = os.path.join(path, target_category)
            os.makedirs(dest_dir, exist_ok=True)

            # Move file
            dest_path = os.path.join(dest_dir, item)
            shutil.move(full_path, dest_path)

            # Terminal output and file logging
            log_entry = f"[MOVED] {item} -> {target_category}/"
            print(log_entry)
            log_file.write(log_entry + "\n")
            moved_count += 1

        summary_line = f"Summary: {moved_count} Files Moved, {skipped_dir_count} Subdirectories Skipped\n"
        print(f"\n{summary_line.strip()}")
        log_file.write(summary_line)