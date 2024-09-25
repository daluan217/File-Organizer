# utils.py

import os
import shutil

def create_category_folders(output_directory, categories):
    """Create folders for each category."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for category in categories:
        category_path = os.path.join(output_directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    print("Category folders created.\n")

def move_file_to_category(filename, category, output_directory):
    """Move a file to the appropriate category folder."""
    category_path = os.path.join(output_directory, category)
    source_path = os.path.join("files", filename)
    dest_path = os.path.join(category_path, filename)
    shutil.move(source_path, dest_path)
    print(f"{filename} has been moved to {category_path}")
