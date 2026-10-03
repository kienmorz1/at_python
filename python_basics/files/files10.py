import os
def secure_copy(source_file,dest_file):
    with open(source_file,"rb") as source:
        with open(dest_file,"wb") as dest:
            while True:
                chunk = source.read(4096)
                if not chunk:
                    break
                dest.write(chunk)

secure_copy("file10.bin","file10_copy.bin")