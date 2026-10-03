def dump_log(log_content):
    with open("sys.log","a+") as file:
        payload = log_content+"\nSYSTEM_OK\n"
        len_of_payload = len(payload)
        file.write(log_content+"\nSYSTEM_OK\n")
        file_size = file.tell()
        file.seek(file_size-len_of_payload)
        verify_content = file.read(len_of_payload)
        if log_content in verify_content:
            print(f"Register log: {log_content}")
        else:
            print(f"{log_content} not registered")

dump_log("hello World")
dump_log("What the hell!!!")