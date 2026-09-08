from pathlib import Path

folder = Path("data")
file= folder / "marks.txt"

print(file)    
print(file.name)    
print(file.suffix)    
