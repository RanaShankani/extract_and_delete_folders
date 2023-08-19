import os
import shutil

def extract_and_delete_folders(root_folder):
    for foldername in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, foldername)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                # Extract the file
                shutil.move(file_path, root_folder)
            # Delete the folder
            shutil.rmtree(folder_path)

# Specify the root folder containing the nested folders
root_folder = "F:\Python\Arrythmia Prediction\ptbdb - Copy (3)"

# Call the function to extract and delete folders
extract_and_delete_folders(root_folder)