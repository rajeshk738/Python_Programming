import csv

with open("F:\\file.csv","r") as file:
    reader = csv.DictReader(file)


for row in reader:
    print(row["Rajesh"])
