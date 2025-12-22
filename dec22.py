# bytes DataType
# It is Immutable data type used for file handling and networking

b = bytes()
print(b,type(b))

b1 = bytes(65)
print(b,type(b1))

b2 = bytes("Hello", "utf-8")
print(b2,type(b2))

b3 = bytes([65,66,67,68,69])
print(b3,type(b3))   # Print ASCII code
print(b3[0])



# bytesarray --> It is array of bytes 
ba = bytearray()
print(ba,type(ba)) 

baa = bytearray("Python", "utf-8")
print(baa,type(baa)) 

baa.append(65)
print(baa)