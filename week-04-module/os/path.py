from pathlib import Path
path = Path("students.txt")

check_exist=path.exists() 
if check_exist==True:
    print(f'file : {path.name}')
    print(f"Extension : {path.suffix}")