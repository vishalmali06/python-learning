from pathlib import Path

# Define directory and file path
data_dir = Path.home() / "Projects" / "python-learning" / "Data"
data_dir.mkdir(parents=True, exist_ok=True)  # Ensure directory exists

file_path = data_dir / "data.txt"


def process_file():
    try:
        # Try opening file in read mode
        with open(file_path, "r") as f:
            x = 1 / 0
            print(f.read())

    except FileNotFoundError:
        print("File not found. Creating the file...")

        # Create the file
        file_path.touch()

        print("File created successfully.")

    finally:
        print("cleaning up the file...")


process_file()
