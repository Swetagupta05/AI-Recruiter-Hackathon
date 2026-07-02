from pathlib import Path

# Locate the project's data folder
project_root = Path(__file__).resolve().parent.parent
data_folder = project_root / "data"

print("=" * 50)
print("FILES INSIDE DATA FOLDER")
print("=" * 50)

for file in data_folder.iterdir():
    print(file.name)