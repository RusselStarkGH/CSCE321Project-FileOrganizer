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

    # Inverts config dict for faster lookups (extension category)
    def _build_reverse_map(self):
        extension_map = {}
        for category, extensions in FILE_CATEGORIES.items():
            for ext in extensions:
                extension_map[ext.lower()] = category
        return extension_map

    # This gets the category of a file, returns 'Other' if unknown
    def get_category(self, file_extension):
        return self._reverse_map.get(file_extension.lower(), "Others")

    # This goes through the source directory to move files
    def organize(self):
        if not self.source.exists():
            logger.error(f"Sourcedirectory {self.source} does not exist.")
            return

        self.dest.mkdir(parents=True, exist_ok=True)

        moved_count = 0

        for file_path in self.source.iterdir():
            if file_path.is_file():
                category = self.get_category(file_path.suffix)
                target_folder = self.dest / category

                target_folder.mkdir(exist_ok=True)

                target_path = target_folder / file_path.name

                try:
                    if not target_path.exists():
                        shutil.move(str(file_path), str(target_path))
                        logger.info(f"Moved: {file_path.name} -> {category}")
                        moved_count += 1
                    else:
                        logger.warning(f"Skipped (Already Exists): {file_path.name}")
                except Exception as e:
                    logger.error(f"Error moving {file_path.name}: {e}")

        logger.info(f"Organization complete. Moved {moved_count} files.")
        print(f"Done, successfully moved {moved_count} files.")