# Config file for the app

# File categories and their extensions
FILE_CATEGORIES = {
    "Documents": ["pdf", "docx", "doc", "txt", "xlsx", "xls", "pptx", "ppt", "csv", "odt", "ods", "odp", "rtf", "md", "epub"],
    "Images": ["jpg", "jpeg", "png", "gif", "svg", "bmp", "webp", "tiff", "tif", "ico", "raw", "heic"],
    "Media": ["mp4", "mp3", "avi", "mkv", "mov", "wav", "flac", "aac", "ogg", "wma", "wmv", "m4a", "m4v", "webm"],
    "Archives": ["zip", "rar", "tar", "gz", "7z", "bz2", "xz", "iso"],
    "Executables": ["exe", "msi", "dmg", "sh", "bat", "cmd", "apk", "appimage"],
    "Code": ["py", "java", "cpp", "c", "cs", "js", "ts", "html", "css", "php", "rb", "go", "rs", "swift", "kt", "json", "xml", "yaml", "yml", "sql"],
    "Fonts": ["ttf", "otf", "woff", "woff2"],
    "3D": ["obj", "fbx", "stl", "blend", "dae"],
    "Disk Images": ["vmdk", "vdi", "vhd", "img"],
}

IGNORED_EXTENSIONS = {
    "tmp", "temp", "log", "cache", "lock"
}

IGNORED_FILES = {
    "desktop.ini", "thumbs.db", "ntuser.dat", "ntuser.ini",
    "pagefile.sys", "hiberfil.sys", ".ds_store", ".localized",
    ".apdisk", ".directory", ".hidden"
}

# Where the unorganized files will go
SOURCE_DIRECTORY = "C:/Users/username/Desktop/TestDownloads"

# Where the organized files will go
DESTINATION_DIRECTORY = "C:/Users/username/Desktop/TestOrganized"