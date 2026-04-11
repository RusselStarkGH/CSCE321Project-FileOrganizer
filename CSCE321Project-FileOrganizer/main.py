from config import SOURCE_DIRECTORY, DESTINATION_DIRECTORY
from organizer import FileOrganizer

def main():
    print(f"Starting organizer for directory: {SOURCE_DIRECTORY}")

    organizer = FileOrganizer(SOURCE_DIRECTORY, DESTINATION_DIRECTORY)
    organizer.organize()

if __name__ == "__main__":
    main()