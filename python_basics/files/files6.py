with open("file6.txt","r+") as file_content:
    content = file_content.read()
    if "VERSION=1.0" in content:
        updated_content = "## LOG START##\n" + content
        file_content.seek(0)
        file_content.write(updated_content)
        file_content.truncate()
    file_content.seek(0)
    print(file_content.read())