def update_and_preview(new_reading):
    with open("file8.txt","a+") as file:
        file.write(new_reading+"\n")
        file.seek(0)
        print(file.read())

update_and_preview("line1")
update_and_preview("line2")
update_and_preview("line3")