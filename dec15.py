# Tuples are immutable sequences in Python, meaning once they are created, their elements cannot be changed, added, or removed.
m =  ()
print(m)
print(type(m))
print("Id of tuple b:",id(m))

q = ("Atharva")# This is a string, not a tuple bcoz for tuple it must have a comma
print(type(q))   
p = ("Atharva",)  # single element tuple
print(type(p))
g = (10,)
print(type(g))

t = (10,20.5,"sai",True,90,10)
print(id(t))

t = (10,20.5,"sai",True,90,10,45)
print(id(t)) # new id because tuples are immutable

# Since tuples are immutable, any change to a tuple results in a new tuple thus we can not perform indexing or slicing operations that modify the tuple itself.
# Thus tuple are generally faster than lists for iteration and access operations.



e1 = "Shirt"
e2 = "Jeans"
e3 = "T-Shirt"
e4 = "Cash"
# Packing is possible without parentheses in tuples
bag = e1,e2,e3,e4,4000 
print(bag)
print(type(bag))
# unpacking of data is also possible in tuples
a,b,c,d,e = bag  
print(a)
print(b)
print(c)
print(d)
print(e)


l1 = "Shirt"
l2 = "Jeans"
l3 = "T-Shirt"
l4 = "Cash"
# Paacking of list is not possible without square brackets
l = [l1,l2,l3,l4,4000]  
print(l)
print(type(l))
# unpacking of list is also possible
p,q,r,s,t = l  
print(p)
print(q)
print(r)
print(s)
print(t)

# Conclusion: Both tuples and lists support unpacking but only tuples support packing


#Indexing and Slicing in tuples
op = (10,20,30,40,50,60,70,80,90)
print(op[-1])# Accessing last element
print(op[2:5])# Slicing from index 2 to 4
print(op[:4])# Slicing from start to index 3
print(op[2])# Accessing element at index 2
print(op[2:])# Slicing from index 2 to end

# Type cating of data using tuple function & list function
lop = (10,20,30,40,50)
zop = [100,200,300,400,500]
print(type(lop))
print(type(zop))
converted_list = list(lop)
converted_tuple = tuple(zop)
print(type(converted_list))
print(type(converted_tuple))

converted_list.append(60)# Adding element to the converted list
again_converted_tuple = tuple(converted_list)# Converting back to tuple
print(again_converted_tuple)# Printing the final tuple after modifications









# HOME WORK
# Q1. Add tuple in list and process the list
# Creating a list
my_list = ["Atharva", 21, "Python"]

# Creating a tuple
my_tuple = ("Coding", "AI", "ML")

# Adding tuple into list
my_list.append(my_tuple)

print("List after adding tuple:")
print(my_list)

# Processing the list

# Indexing
print("\nIndexing:")
print("Element at index 0:", my_list[0])
print("Tuple inside list:", my_list[3])

# Slicing
print("\nSlicing:")
print(my_list[1:3])

# Pop operation
removed_item = my_list.pop()
print("\nAfter pop():")
print(my_list)
print("Popped item:", removed_item)

# Append operation
my_list.append("Developer")
print("\nAfter append():")
print(my_list)

# Insert operation
my_list.insert(1, "Student")
print("\nAfter insert():")
print(my_list)

# Remove operation
my_list.remove(21)
print("\nAfter remove():")
print(my_list)
 
# Q2. Add list in tuple and process the tuple
# Creating a tuple
my_tuple = ("Atharva", "Python", 2025)

# Creating a list
my_list = ["AI", "ML", "Data Science"]

# Adding list into tuple (by converting tuple to list)
temp = list(my_tuple)
temp.append(my_list)

# Converting back to tuple
my_tuple = tuple(temp)

print("Tuple after adding list:")
print(my_tuple)

# Processing the tuple

# Indexing
print("\nIndexing:")
print("Element at index 0:", my_tuple[0])
print("List inside tuple:", my_tuple[3])

# Slicing
print("\nSlicing:")
print(my_tuple[1:3])

# Accessing elements inside the list in tuple
print("\nAccessing list elements:")
print(my_tuple[3][0])
print(my_tuple[3][1])

# Removing element (convert to list)
temp = list(my_tuple)
temp.pop(1)
my_tuple = tuple(temp)

print("\nAfter pop operation:")
print(my_tuple)
