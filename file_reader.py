# file_reader.py

import os

class FileReader:
    def __init__(self, directory):
        self.directory = directory

    def get_files(self):
        """Return a list of all text files in the directory."""
        files = [f for f in os.listdir(self.directory) if f.endswith('.txt')]
        return files

    def read_file(self, filename):
        """Read the content of a file and return it as a string."""
        with open(os.path.join(self.directory, filename), 'r') as file:
            return file.read()
