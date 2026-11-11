from pathlib import Path
import shutil

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

def organize_files(files, directory):
    """
    Organize files and track the number moved into each category.

    Returns:
        A dictionary containing the number of files per category.
    """
    category_counts = {}

    for file in files:
        category = categorize_file(file)
        move_file(file, category, directory)

        category_counts[category] = (
            category_counts.get(category, 0) + 1
        )

    return category_counts

def display_report(category_counts):
    """
    Display a summary of the organization process.
    """
    total_files = sum(category_counts.values())

    print("\n========== ORGANIZATION COMPLETE ==========")
    print(f"\nFiles organized: {total_files}\n")

    for category in list(CATEGORIES) + ["Other"]:
        count = category_counts.get(category, 0)

        if count > 0:
            print(f"{category}: {count}")

    print("\nOperation completed successfully!")
    print("============================================")

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
        destination = directory / category
    
        target = get_unique_destination(destination, file.name)
    
        relative_target = target.relative_to(directory)
    
        print(f"{file.name} -> {relative_target}")

    print("\n==========================================")
    print(f"Total files to organize: {len(files)}")

def confirm_action():
    """
    Ask the user whether to proceed with organization.

    Returns:
        True if the user confirms, False otherwise.
    """
    while True:
        answer = input("\nProceed with organization? (y/n): ").strip().lower()

        if answer == "y":
            return True

        if answer == "n":
            return False

        print("Invalid input. Please enter 'y' or 'n'.")

def get_unique_destination(destination, filename):
    """
    Generate a unique destination path to prevent overwriting files.

    If the filename already exists, append a number before
    the extension (e.g. homework_1.pdf).
    """
    destination = Path(destination)
    original_file = Path(filename)

    target = destination / filename
    counter = 1

    while target.exists():
        new_name = (
            f"{original_file.stem}_{counter}"
            f"{original_file.suffix}"
        )
        target = destination / new_name
        counter += 1

    return target


def move_file(file, category, directory):
    """
    Move a file into its category folder without overwriting.
    """
    destination = directory / category

    # Create category folder if necessary.
    destination.mkdir(exist_ok=True)

    # Generate a unique filename.
    target = get_unique_destination(destination, file.name)

    # Move the file.
    shutil.move(str(file), str(target))


def main():
    print("===== SMART FILE ORGANIZER =====")

    directory = input("Enter directory path: ").strip()

    try:
        path = Path(directory)
        files = scan_directory(path)

        print(f"\nFound {len(files)} files.")

        preview_organization(files, path)
                
        if confirm_action():
            category_counts = organize_files(files, path)
            display_report(category_counts)
        else:
            print("\nOrganization cancelled.")
                    
    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()

