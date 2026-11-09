
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


def preview_organization(files, directory):
    """
    Display the planned organization without moving files.

    Args:
        files: List of files to organize.
        directory: The directory being organized.
    """
    print("\n========== ORGANIZATION PREVIEW ==========")

    if not files:
        print("No files to organize.")
        return

    for file in files:
        category = categorize_file(file)
        destination = directory / category / file.name

        print(f"{file.name} -> {category}/{file.name}")

    print("\n==========================================")
    print(f"Total files to organize: {len(files)}")


def main():
    print("===== SMART FILE ORGANIZER =====")

    directory = input("Enter directory path: ").strip()

    try:
        path = Path(directory)
        files = scan_directory(path)

        print(f"\nFound {len(files)} files.")

        preview_organization(files, path)

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()

