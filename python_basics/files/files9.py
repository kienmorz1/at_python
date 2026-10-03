ROW_SIZE = 20
TARGET_ROW = 1
NAME_OFFSET = 13

seek_position = (ROW_SIZE*TARGET_ROW) + NAME_OFFSET
with open("file9.db","r+") as file:
    file.seek(seek_position)
    new_name = "Jaffa"
    padded_name = f"{new_name:<8}"
    file.write(padded_name)
    file.seek(0)
    print(file.read())