import os
import shutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define source directory and destination directories
source_dir = 'pathtoyourdownloads'  # Replace with the path to your downloads directory
dest_dirs = {
    'Documents' ['.pdf', '.docx', '.txt'],
    'Images' ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos' ['.mp4', '.mov', '.avi'],
    'Music' ['.mp3', '.wav', '.aac'],
    'Archives' ['.zip', '.tar', '.rar']
}

def create_directory(directory)
    Create directory if it doesn't exist
    if not os.path.exists(directory)
        os.makedirs(directory)

def move_file(file, dest_dir)
    Move file to the destination directory
    try
        shutil.move(file, dest_dir)
        logging.info(f'Moved file {file} to {dest_dir}')
    except Exception as e
        logging.error(f'Error moving file {file} to {dest_dir} {e}')

def organize_files()
    Organize files in the source directory into designated subdirectories
    for filename in os.listdir(source_dir)
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path)
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in dest_dirs.items()
                if file_ext in extensions
                    category_dir = os.path.join(source_dir, category)
                    create_directory(category_dir)
                    move_file(file_path, category_dir)
                    moved = True
                    break
            if not moved
                # Move files with unknown extensions to an Others directory
                others_dir = os.path.join(source_dir, 'Others')
                create_directory(others_dir)
                move_file(file_path, others_dir)

if __name__ == '__main__'
    try
        logging.info('Starting file organization')
        organize_files()
        logging.info('File organization completed')
    except Exception as e
        logging.error(f'Unexpected error {e}')
