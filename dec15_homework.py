
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
