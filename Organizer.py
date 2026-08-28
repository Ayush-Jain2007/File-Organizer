import os

file_count = 0
dir_count = 0

print("============================================")
print("             FILE ORGANIZER               ")
print("============================================\n")

path = input("Enter folder path:\n> ").strip()

if not os.path.exists(path):
    print("Error: The specified path does not exist.")
elif not os.path.isdir(path):
    print("Error: The path is not a directory.")
else:
    print("\nContents found:\n")
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        
        if os.path.isfile(full_path):
            print(f"[FILE] {item}")
            file_count += 1
        elif os.path.isdir(full_path):  
            print(f"[DIR]  {item}")
            dir_count += 1

print(f"Summary: {file_count} Files, {dir_count} Directories Found")