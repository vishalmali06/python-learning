from pathlib import Path
import json

# ---------------------------------------------------
# Create a dictionary of people and their details
# ---------------------------------------------------

book = {}

book["tom"] = {
    "name": "Tom",
    "address": "123 Main Street",
    "phone": "555-555-556",
}

book["bob"] = {
    "name": "Bob",
    "address": "124 Main Street",
    "phone": "555-555-557",
}

# ---------------------------------------------------
# Define the file path using pathlib (BEST PRACTICE)
# ---------------------------------------------------

data_dir = Path.home() / "Projects" / "python-learning" / "Data"
data_dir.mkdir(parents=True, exist_ok=True)   # Ensure folder exists

file_path = data_dir / "book.json"

# ---------------------------------------------------
# Write dictionary data to JSON file
# ---------------------------------------------------

with open(file_path, "w") as f:
    json.dump(book, f, indent=4)

# ---------------------------------------------------
# Read JSON file and load data back into Python
# ---------------------------------------------------

with open(file_path, "r") as f:
    books = json.load(f)

# ---------------------------------------------------
# Print each person's details
# ---------------------------------------------------

for person in books:
    print(books[person])
