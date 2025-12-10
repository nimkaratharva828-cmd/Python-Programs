c1 = 10 - 20.5j
print(type(c1))# COMPLEX NUMBERS

c2 = 0b101 + 20j
print(c2)# COMPLEX NUMBERS

c3 = 0o123 + 0.5j
print(type(c3))
print(c3)

c4 = 0xface + 89j
print(type(c4))
print(c4)

# c5 = 20 + 0x123j # Note: in Imaginary part only decimal allowed if still you want to write imaginary part with using other int(eg. hexadecimal,octal,binary) you have to use complex() function
# You can not give direct value to j , if you want to give direct value to j then you have to use complex() function
c5 = complex(0b1010, 0xface)
print(type(c5))
print(c5)

b1 = 0b1011
o1 = 0o1234
x1 = 0xface 
print(b1, type(b1))
print(o1, type(o1))
print(x1, type(x1))
# Python always display integer value in decimal format only but if you want to display in other format then you have to use functions like bin(), oct(), hex()
v1 = bin(668)
o1 = oct(0o1234)
v2 = hex(64206)
print(v1, type(v1))
print(o1, type(o1))
print(v2, type(v2))
g = v1 + v2
# As we discussed earlier that python only display integer in decimal format but we forced python to display in other format like binary, octal, hexadecimal thus python ne jugad kiya aur use string main dalkar according to our convinience different form main display kiya kyuki " " string ke double quote main kuch bhi likho wo as it is display hota hai
# Hence when we use bin(), oct(), hex() functions to display integer in different format then those functions return string value
print("Value of v1 is:",v1,"& Value of v2 is:",v2,"& Sum of v1 and v2 is:",g,"and its type is:",type(g))