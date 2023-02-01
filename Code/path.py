from pathlib import Path

base_folder = Path(__file__).parent.resolve()
data_file = base_folder / "data.csv"

with open(data_file, "w", buffering=1) as f:
    for i in range(100):
        f.write(f"Some data: {i}\n")