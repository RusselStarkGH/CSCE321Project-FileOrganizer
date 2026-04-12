# The organizer script for the app

import shutil
from pathlib import Path
from config import FILE_CATEGORIES, IGNORED_FILES, IGNORED_EXTENSIONS
from logger import logger

# This organizes files from the source_dir (dir = directory) to the dest_dir based on their extensions
class FileOrganizer:
    def __init__(self, source_dir, dest_dir, recursive=False, operation="copy"):
        self.source = Path(source_dir)
        self.dest = Path(dest_dir)
        self.recursive = recursive  # Whether to check subdirectories
        self.operation = operation  # Whether to copy or move
        self.operation_text = "copied" if self.operation == "copy" else "moved"
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
        ext = file_extension.lstrip('.').lower()    # Remove the leading dot to stay consistent (no dots in the config)
        return self._reverse_map.get(ext, "Others")

    # Moves a file to the target folder
    def _move_file(self, file_path):
        category = self.get_category(file_path.suffix)
        target_folder = self.dest / category
        target_folder.mkdir(exist_ok=True)
        target_path = target_folder / file_path.name

        try:
            if not target_path.exists():
                if (self.operation == "copy"):
                    shutil.copy2(str(file_path), str(target_path))
                else:
                    shutil.move(str(file_path), str(target_path))

                logger.info(f"{self.operation_text.capitalize()}: {file_path.name} -> {category}")
                return True
            else:
                logger.warning(f"Skipped (Already Exists): {file_path.name}")
                return False
        except Exception as e:
            logger.error(f"Error moving/copying {file_path.name}: {e}")
            return False

    # This goes through the source directory to move files
    def organize(self):
        if not self.source.exists():
            logger.error(f"Sourcedirectory {self.source} does not exist.")
            return

        self.dest.mkdir(parents=True, exist_ok=True)
        moved_count = 0
        files = self.source.rglob("*") if self.recursive else self.source.iterdir()

        for file_path in files:
            if not file_path.is_file():
                continue
            if file_path.resolve().is_relative_to(self.dest.resolve()):     # Don't move if already there
                continue
            if file_path.name.lower() in IGNORED_FILES:
                continue
            if file_path.suffix.lstrip(".").lower() in IGNORED_EXTENSIONS:
                continue
            if file_path.name.startswith("~$"):
                continue

            if self._move_file(file_path):
                moved_count += 1
            
        logger.info(f"Organization complete. {self.operation_text.capitalize()} {moved_count} files.")
        print(f"Done, successfully {self.operation_text} {moved_count} files.")