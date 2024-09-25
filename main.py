# main.py

from organizer import Organizer

def main():
    print("Welcome to the Text File Organizer!")

    # Specify the directory with text files and the output directory
    files_directory = "files"
    output_directory = "organized_files"

    # Create the Organizer and organize files
    organizer = Organizer(files_directory, output_directory)
    organizer.organize_files()

if __name__ == "__main__":
    main()