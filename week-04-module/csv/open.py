# import csv

# with open("student.csv", "r") as f:
#     reader = csv.reader(f)

#     for i in reader:
#         header = next(reader)
#         iter(int(i[2]))
#         iter(int(i[2]))
#         iter(int(i[2]))
#         if i>90:
#             print(i)
import csv

with open("student.csv", "r") as f:
    reader = csv.reader(f)

    header = next(reader)

    for row in reader:
        marks = int(row[2])

        if marks >= 90:
            print(f"{row[0]}: {marks}")