# organizer.py

import os
from keyword_manager import KeywordManager
from file_reader import FileReader
from utils import create_category_folders, move_file_to_category

class Organizer:
    def __init__(self, files_directory, output_directory):
        self.file_reader = FileReader(files_directory)
        self.keyword_manager = KeywordManager()
        self.output_directory = output_directory

    def organize_files(self):
        # Step 1: Get list of files
        files = self.file_reader.get_files()
        print(f"Found {len(files)} files to organize.\n")

        # Step 2: Create category folders
        create_category_folders(self.output_directory, self.keyword_manager.get_categories().keys())

        # Step 3: Process each file
        for file in files:
            content = self.file_reader.read_file(file)
            self._categorize_file(file, content)

    def _categorize_file(self, filename, content):
        categories = self.keyword_manager.get_categories()
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.lower() in content.lower():
                    move_file_to_category(filename, category, self.output_directory)
                    print(f"'{filename}' categorized as '{category}' due to keyword '{keyword}'.")
                    return
        print(f"No category found for '{filename}'. File remains in place.")
