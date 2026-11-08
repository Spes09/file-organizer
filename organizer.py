
from pathlib import Path


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


def main():
    print("===== SMART FILE ORGANIZER =====")

    directory = input("Enter directory path: ").strip()

    try:
        files = scan_directory(directory)

        print(f"\nFound {len(files)} files:\n")

        for file in files:
            print(f"- {file.name}")

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
