with open("file13.dat","wb+") as fb:
    fb.write(b"BAD!\x00\x01\x02TelemetryPayloadDataHere\x00")
    print(fb.tell())
    fb.seek(0)
    print("file content then: ",fb.read())
    

with open("file13.dat","rb+") as rb:
    truncate_target_position = rb.seek(-1,2)
    print(truncate_target_position)
    if rb.read(1) == b'\x00':
        print(rb.tell())
        rb.truncate(truncate_target_position)
    rb.seek(0)
    print("file content now:", rb.read())