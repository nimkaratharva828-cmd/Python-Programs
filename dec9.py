s1 = "instagram" # String using double quotes

s2 = 'insta' # String using single quotes

s3 = """ins ta""" # String using triple double quotes

s4 = """This is a multi-line string.
It can span multiple lines.
        Menu
        1. Home
        2. Profile
        3. Settings"""
        
s5 = '''insta @12#4f5v'''


print(s1,type(s1),"and length is",len(s1))
print(s2,type(s2),"and length is",len(s2))
print(s3,type(s3),"and length is",len(s3))
print(s4,type(s4),"and length is",len(s4))
print(s5,type(s5),"and length is",len(s5))

# Indexing operations

print(s1[0]) # First character
print(s1[-9]) # First character using negative indexing

p = s1[8]
q = s1[len(s1)-1]
r = s1[-1]
print(p) # Last character
print(q) # Last character using length function
print(r) # Last character using negative indexing


result1 = s1[0]
result2 = s1[1]
result3 = s1[2:4]
result4 = s1[4:]
result_total = result1 + result2 + result3 + result4 # It is a concatenation operation of string not an addition...addition is possible only of numbers
print(result_total,type(result_total))

j1 = s1[6]
j2 = s1[7]
j3 = s1[8]
j = j1 + j2 + j3
print(j,type(j)) #Printing ram from instagram using forward indexing
j4 = s1[-1]
j5 = s1[-2]
j6 = s1[-3]
j7 = j6 + j5 + j4
print(j7,type(j7)) #Printing ram from instagram using negative indexing


l1 = s1[3]
l2 = s1[4]
l3 = s1[5]
l4 = l1 + l2 + l3
print(l4,type(l4)) #Printing tag from instagram using forward indexing
l5 = s1[-4]
l6 = s1[-5]
l7 = s1[-6]
l = l7 + l6 + l5
print(l,type(l)) #Printing tag from instagram using negative indexing


k1 = s1[0:5]
print(k1) 

p1 = s1[:-5]
print(p1)

print(s1[9]) # Index out of range error for more than length of string