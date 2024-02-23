import os
import subprocess

favorite_folders = [
    "E:/Self_Learning",
    "E:/asu",
    "E:/Self_Learning/Embedded IMT"
]

# Display available folders to the user
for i, folder in enumerate(favorite_folders):
    print(f"{i}: {folder}")

try:
    val = int(input("Please select your directory (index starts with 0): "))
    if val < 0 or val >= len(favorite_folders):
        raise ValueError("Invalid index")
except ValueError:
    print("Invalid input. Please enter a valid index.")
else:
    # Open the selected folder using the default file manager
    folder_path = favorite_folders[val]
    if os.name == 'nt':
        os.startfile(folder_path)
    elif os.name == 'posix':
        subprocess.run(["xdg-open", folder_path])
    else:
        print("Unsupported operating system.")
