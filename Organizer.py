import os
import shutil

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"]
}

print("============================================")
print("             FILE ORGANIZER v2.0            ")
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

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        # Skip subdirectories so we don't move existing folders
        if os.path.isdir(full_path):
            skipped_dir_count += 1
            continue

        # Extract file extension and normalize to lowercase
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        # Find matching category folder
        target_category = "Others"
        for category, extensions in CATEGORIES.items():
            if ext in extensions:
                target_category = category
                break

        # Create destination directory if it doesn't exist
        dest_dir = os.path.join(path, target_category)
        os.makedirs(dest_dir, exist_ok=True)

        # Move file to destination folder
        dest_path = os.path.join(dest_dir, item)
        shutil.move(full_path, dest_path)

        print(f"[MOVED] {item} -> {target_category}/")
        moved_count += 1

    print(f"\nSummary: {moved_count} Files Moved, {skipped_dir_count} Subdirectories Skipped")