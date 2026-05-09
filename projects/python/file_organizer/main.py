import shutil
from pathlib import Path

# Define the directory to clean 
root_dir = Path("D:/Program/Python/projects/python/file_organizer/data")

# Define your categories
file_cetegories = {
    "Images":[".jpg",".jpeg",".png",".gif",".bmp",".tiff",".webp"],
    "Documents":[".pdf",".doc",".docx",".txt",".ppt",".pptx",".xls",".xlsx",".csv",".md"],
    "Videos":[".mp4",".mov",".avi",".mkv",".wmv",".flv",".webm"],
    "Audio":[".mp3",".wav",".aac",".flac",".ogg",".m4a"],
    "Archives":[".zip",".rar",".7z",".tar",".gz"],
    "Code":[".py",".html",".css",".js",".json",".xml",".c",".cpp",".java",".php",".rb"],
    "Executables":[".exe",".msi",".dmg",".pkg",".deb",".rpm"]
}

def organize_files():
    for file_path in root_dir.iterdir():
        if file_path.is_file():
            # Get the extension
            ext = file_path.suffix.lower()

            # find the category
            for category, extensions in file_cetegories.items():
                if ext in extensions:
                    dest_folder = root_dir / category
                    dest_folder.mkdir(exist_ok=True)
                    shutil.move(str(file_path), str(dest_folder / file_path.name))
                    print(f"Moved: {file_path.name} -> {category}")

if __name__ == '__main__':
    organize_files()