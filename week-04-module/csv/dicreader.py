import csv

with open ("student.csv","r") as f:
    reader=csv.DictReader(f)
    
    for row in reader:
        marks=int(row['marks'])
        if marks>90:  
            print(f'{row["name"]}:{row["marks"]}')