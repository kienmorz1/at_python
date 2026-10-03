import json
content = [{"status":"INIT"},{"status":"RUNNING"}]
with open("files12.json","w") as json_file:
    json_file.write(json.dumps(content))

with open("files12.json","r+") as json_file:
    new_content = ",{\"status\": \"SUCCESS\"}]"
    json_file.seek(0,2)
    file_size = json_file.tell()
    json_file.seek(file_size-1)
    json_file.write(new_content)
    json_file.read()