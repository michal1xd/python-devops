import os

# Define the structure of our project
project_name = "my_awesome_project"
subfolders = ["src", "docs", "tests", "config"]

print(f"Setting up directory structure for '{project_name}'...")

# Create the main project directory if it doesn't exist
os.makedirs(project_name, exist_ok=True)

# Loop through the list and create each subfolder
for folder in subfolders:
    # We use os.path.join() to create a correct path for any OS (Win, Mac, Linux)
    path_to_create = os.path.join(project_name, folder)
    
    # Create the directory
    os.makedirs(path_to_create, exist_ok=True)
    
    print(f"  -> Created directory: {path_to_create}")

print("\nProject structure created successfully!")