import csv
print("\nExample: CSV File")

with open("student.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Sachine", 28])
    writer.writerow(["Dhoni", 29])
    writer.writerow(["Khlli", 30])

with open('student.csv',"r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)