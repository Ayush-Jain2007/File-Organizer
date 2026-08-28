import os
import shutil
from datetime import datetime

class FileOrganizer:
    """An object-oriented file organizer that categorizes files and logs actions."""
    
    # Class-level constants
    CATEGORIES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
        "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".flac"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"]
    }
    LOG_FILE_NAME = "organizer_log.txt"

    def __init__(self, target_path):
        """Initializes the organizer with a specific target directory."""
        self.target_path = target_path
        self.log_file_path = os.path.join(self.target_path, self.LOG_FILE_NAME)

    def is_valid_path(self):
        """Validates if the provided path exists and is a directory."""
        if not os.path.exists(self.target_path):
            print("Error: The specified path does not exist.")
            return False
        if not os.path.isdir(self.target_path):
            print("Error: The path is not a directory.")
            return False
        return True

    def organize(self):
        """Organizes files into categorized subfolders and logs the actions."""
        if not self.is_valid_path():
            return

        print("\nOrganizing files...\n")
        moved_count = 0
        skipped_dir_count = 0

        with open(self.log_file_path, "a", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"\n--- Execution Run: {timestamp} ---\n")

            for item in os.listdir(self.target_path):
                if item == self.LOG_FILE_NAME:
                    continue

                full_path = os.path.join(self.target_path, item)

                if os.path.isdir(full_path):
                    skipped_dir_count += 1
                    continue

                _, ext = os.path.splitext(item)
                ext = ext.lower()

                target_category = "Others"
                for category, extensions in self.CATEGORIES.items():
                    if ext in extensions:
                        target_category = category
                        break

                dest_dir = os.path.join(self.target_path, target_category)
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

    def view_logs(self):
        """Reads and displays the log history."""
        if not self.is_valid_path():
            return

        if not os.path.exists(self.log_file_path):
            print(f"\nNo previous log file ('{self.LOG_FILE_NAME}') found in this directory.")
            return

        print(f"\n================ LOG HISTORY ================")
        with open(self.log_file_path, "r", encoding="utf-8") as log_file:
            content = log_file.read()
            if content.strip():
                print(content)
            else:
                print("[Log file is empty]")
        print("=============================================")


def main():
    print("============================================")
    print("             FILE ORGANIZER v5.0            ")
    print("           (Object-Oriented Edition)        ")
    print("============================================\n")
    
    path = input("Enter folder path to manage:\n> ").strip()
    
    # Instantiate the object
    organizer = FileOrganizer(path)

    # Infinite loop for continuous menu use until the user exits
    while True:
        print("\n1. Organize Directory")
        print("2. View Log History")
        print("3. Exit Program")
        
        choice = input("\nSelect an option (1, 2, or 3):\n> ").strip()
        
        if choice == "1":
            organizer.organize()
        elif choice == "2":
            organizer.view_logs()
        elif choice == "3":
            print("Exiting File Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()