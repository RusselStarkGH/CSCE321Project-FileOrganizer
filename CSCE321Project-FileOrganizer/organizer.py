# The organizer script for the app

import shutil
from pathlib import Path
from config import FILE_CATEGORIES
from logger import logger

# This organizes files from the source_dir (dir = directory) to the dest_dir based on their extensions
class FileOrganizer:
    def __init__(self, source_dir, dest_dir):
        self.source = Path(source_dir)
        self.dest = Path(dest_dir)
        self._reverse_map = self._build_reverse_map()

    # This organizes the files by moving them to the category folders in the dest_dir
    def _build_reverse_map(self):
        extension_map = {}
        for category, extensions in FILE_CATEGORIES.items():
            for ext in extensions:
                extension_map[ext.lower()] = category
                return extension_map

# Still unfinished, I need to implement more funtions for this class to properly work.
