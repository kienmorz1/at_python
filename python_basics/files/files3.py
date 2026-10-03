fruits = ["apple\n", "banana\n", "cherry\n", "date\n", "elderberry\n"]
FILE_NAME = "grocery.txt"

with open(FILE_NAME, "w") as file:
    for fruit in fruits:
        file.write(fruit)

with open(FILE_NAME,"r") as file:
    print(file.read())

with open(FILE_NAME,"w") as file:
    file.writelines(fruits)

with open(FILE_NAME,"r") as file:
    print(file.read())