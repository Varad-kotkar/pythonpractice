from pathlib import Path

folder = Path("data")
folder.mkdir(exist_ok=True)
file= folder / "students.txt"