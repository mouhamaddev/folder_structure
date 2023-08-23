import os

# Define the directory where you want to create the folders
base_directory = "main"

# Define the folder structure as a nested dictionary
folder_structure = {
    "folder_1": {
        "subfolder_1.1: {},
        "subfolder_1.2": {}
    },    
    "folder_2": {
        "subfolder_2.1": {
            "subfolder_2.1.1": {},
            "subfolder_2.1.2": {}
        },
    }
}

# Function to create folders recursively
def create_folders(directory, structure):
    for folder, subfolders in structure.items():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
        if subfolders:
            create_folders(folder_path, subfolders)

# Create the folders
create_folders(base_directory, folder_structure)

print("Folders and subfolders created successfully.")

