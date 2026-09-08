from pathlib import Path

folder = Path("reports")

folder.mkdir(exist_ok=True)

file = folder / "marks.txt"

if file.exists():
    print(file)