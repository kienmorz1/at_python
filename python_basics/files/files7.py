with open("file7.dat","wb") as fb:
    fb.write(b"BAD!\x00\x01\x02TelemetryPayloadDataHere")


with open("file7.dat","rb+") as fb:
    header = fb.read(4)
    if b"BAD!" == header:
        fb.seek(0)
        fb.write(b"DATA")
    fb.seek(0)
    print(fb.read())