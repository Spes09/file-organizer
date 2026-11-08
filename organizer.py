
from pathlib import Path

CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".doc"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Executable": [".exe"]
}

def scan_directory(directory):
    """
    Scan a directory and return all files inside it.

    Args:
        directory: Path to the directory to scan.

    Returns:
        A list of file paths.

    Raises:
        ValueError: If the directory does not exist or is invalid.
    """
    path = Path(directory)

    if not path.exists():
        raise ValueError("Directory does not exist.")

    if not path.is_dir():
        raise ValueError("The provided path is not a directory.")

    files = []

    for item in path.iterdir():
        if item.is_file():
            files.append(item)

    return files

def categorize_file(file):
    """
    Determine the category of a file based on its extension.

    Args:
        file: Path object representing a file.

    Returns:
        The file's category, or Other if unknown.
    """
    extension = file.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"

def main():
    print("===== SMART FILE ORGANIZER =====")

    directory = input("Enter directory path: ").strip()

    try:
        files = scan_directory(directory)

        print(f"\nFound {len(files)} files:\n")

        for file in files:
            category = categorize_file(file)
            print(f"- {file.name} -> {category}")

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()

