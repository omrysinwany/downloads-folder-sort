"""
Downloads folder sorter

This script iterates through the files in a user's downloads folder on Windows and places each file in its appropriate
folder.

This file contains the following functions:

    * move_file - checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    * sort_folder - iterates through the files in the folder
"""

import json
import shutil
from pathlib import Path


def move_file(file, destination):
    """Checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    Parameters
    ----------
    file
        the path to a file
    destination
        the path to the destination folder
    """
    try:
        if not destination.exists():
            destination.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file), str(destination))
    except shutil.Error as e:
        print(e)


def sort_folder(folder_path):
    """
    Iterates through the files in the folder, sorting them into sub-folders by extension.
    Parameters
    ----------
    folder_path
        the path to the folder to be organized
    """
    with open('config.json', encoding='utf-8') as f:
        categories = json.load(f)

    extensions_map = {}
    for category in categories:
        folder_name = category['name']
        for extension in category['extensions']:
            extensions_map[extension] = folder_name

    for file in folder_path.iterdir():
        if file.is_file() and not file.name.startswith('.'):
            destination = extensions_map.get(file.suffix, 'Other')
            move_file(file, file.parent.joinpath(destination))


if __name__ == '__main__':
    home_directory = str(Path.home())
    download_path = Path(f'{home_directory}/Downloads')

    sort_folder(download_path)
