r = range(1,11)  # Syntax: range(Start_value, End_value)
print(r)
print(type(r))
for i in r:    # Printing values in the range using for loop
    print(i)
print(list(r)) # Printing values in the range using list() function
print(tuple(r))  # Printing values in the range using tuple() function

r1 = range(31) # Syntax: range(End_value)
print(list(r1))

r2 = range(1,20,2)  # Syntax: range(Start_value, End_value, Step_value)
print(list(r2))

# Print table of 2 using range()
p = range(2,41,2)
print("Table of 2:")
for i in p:
    print(i)
    
# Print table of 3 using range()
j = range(3,31,3)
print("Table of 3:")
for m in j:
    print(m)
    
# Print values from 20 to 3 with a step size of 3
k = range(20,2,-3)
print("Values from 20 to 3 with a step size of 3:")
for n in k:
    print(n)
    
# Generating negatives values
g = range(-1,-10,-2)
print("Negative values from -1 to -10 with a step size of -2:")
for v in g:
    print(v)
    
print("Even numbers from 2 to 20:")
for f in range(2,21,2):
    print(f)
 
 
print("Table of 5:")   
lop=1
mno = range(5,51,5)
for mg in mno:
    print(f"5 x {lop} =",mg)
    lop = lop+1
    
    
# Iterate string using ranage

s = "Instagram"

# Here we are using range to get controll of the index
for k in range(0, len(s)):
    print(k,"---------->",s[k])
    
# Here we just have controll on the elements itself , to get controll of their index we need to use range     
for k in s:
    print(k)     
     
     
        
# for k in range(0, len(s)):
#      if k % 2 == 1:
#          print(k,"---------->",s[k])
    
    
    
print("Operations on list using Range()")   
list = [23,34,45,56,67]
for i in range(len(list)):
    print(i)  
print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
for i in range(len(list)-1,-1,-1):
    print(i)
    
# Now we want square of values present at even index(0,2,4)
# And cube of values present at odd index(1,3)
# In short we want controll on the indexes of each elements
chotu_sq_list = []
chotu_cube_list=[]

for i in range(len(list)):
    if i % 2 ==0:
        chotu_sq_list.append(list[i] * list[i]) 
    else:
        chotu_cube_list.append(list[i] * list[i] * list[i])
print("Original list: ",list)
print("Square list: ",chotu_sq_list)
print("Cube list: ",chotu_cube_list)



