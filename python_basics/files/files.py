
text_input = ["This is a sample file.\n","Python file I/O files\n"]

with open("hello.txt", 'w') as file:
    file.write("Hello!! just testing\n")
    file.writelines(text_input)
    
with open("hello.txt","r") as file:
    print("Reading first line: ")
    print(file.readline())
    print("Reading second line: ")
    print(file.readline())
    print("Reading third line: ")
    print(file.readline())
    
with open("hello.txt","a") as file:
    file.write("Added A newline")

with open("hello.txt","r") as file:
    print(file.readlines())