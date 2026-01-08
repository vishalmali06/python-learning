from pathlib import Path

# ---------------------------------------------------
# Setup directory and file paths
# ---------------------------------------------------

data_dir = Path.home() / "Projects" / "python-learning" / "Data"
data_dir.mkdir(parents=True, exist_ok=True)

file_path = data_dir / "funny.json"
file_path_wc = data_dir / "funny_wc.json"

# ---------------------------------------------------
# Read input file and write word count to output file
# ---------------------------------------------------

with (
    open(file_path, "r") as input_file,
    open(file_path_wc, "w") as output_file
):
    for line in input_file:
        tokens = line.strip().split()
        word_count = len(tokens)

        print(word_count)
        output_file.write(
            "wordcount: " + (f"0{word_count}" if word_count < 10 else str(word_count)) + " " + line
        )
