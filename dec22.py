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
# bytearray-->mutable 
ba = bytearray()
print(ba,type(ba)) 

baa = bytearray("Python", "utf-8")
print(baa,type(baa)) 

baa.append(65)
print(baa)

# None datatype  ---> not zero not empty
var = None
print(var)
print(type(var))

# Below all functions(print,datatype,id) returns something
print("Hwllo, World!")
v1 = "Python"
datatype = type(v1)
print(datatype)
address = id(v1)
print(address)

res = print("Python") # Here output is none bcoz print returns nothing thus its datatype is none
print("Result is---->",res) 
print()
print()
print()
print(print("Python")) # inner print function will print python but itself provides nothing thus outer print get none therefore we get first python then none
print()
print()
print()

print(print("Atharva",print("Python")))



# OPERATORS

ab = {10:"Poly",20:"Diploma"}
abc = {100:"Polyy",200:"Diplomaa"}
print("Addition=",ab+abc) # TypeError:unsupported operand type(s) for +: 'dict' and 'dict'

