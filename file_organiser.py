# Import modules for file handling and moving files
import os
import shutil
from datetime import datetime

# Folder containing files to organise
source_folder = "test-files"

# Dictionary mapping file extensions to folder names
file_types = {
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".csv": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Videos",
    ".mov": "Videos"
}

# Track how many files are moved
moved_files = 0

# Open log file in append mode so previous logs are preserved
log_file = open("organiser_log.txt", "a")

# Process every item inside the source folder 
for file_name in os.listdir(source_folder):
    source_path = os.path.join(source_folder, file_name)

    # Only organise files and ignore folders
    if os.path.isfile(source_path):

        # Separate filename and extension
        name, extension = os.path.splitext(file_name)

        # Standardise extension matching
        extension = extension.lower()

        # Use matching folder name or "Other" for unknown types
        folder_name = file_types.get(extension, "Other")

        # Create destination folder path
        destination_folder = os.path.join(source_folder, folder_name)

        # Warn about unsupported file types
        if folder_name == "Other":
            print(f"Unknown file type: {file_name}")

        # Create folder if it does not already exist 
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Move file into destination folder
        destination_path = os.path.join(destination_folder, file_name)
        
        # Check if a file with the same name already exists
        if os.path.exists(destination_path):
            name, extension = os.path.splitext(file_name)

            # Start dublicate counter at 1
            counter = 1

            # Keep generating new names until a free one is found
            while os.path.exists(destination_path):

                # Create new file name like file_1.png
                new_file_name = f"{name}_{counter}{extension}"

                # Build updated destination path
                destination_path = os.path.join(destination_folder, new_file_name)
                
                counter += 1

        # Move file into destination folder
        shutil.move(source_path, destination_path)

        moved_files += 1

        # Log file movement
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp}] Moved {file_name} to {destination_path}"
        print(message)
        log_file.write(message + "\n")

# Close file after script finishes 
log_file.close()

# Display final summary
print(f"\nFinished organising {moved_files} files.")