# Today we learn about Python Lists
# A list is a collection which is ordered and changeable. In Python, lists are written with square brackets seperated by comma.

groceryList = ["abc 1kg","pqr 3 kg","Atharva","Neha"]

print(type(groceryList))
print(groceryList)
print(id(groceryList))

# TO create an empty list
m = []
print(type(m))
print(m)
print(id(m))

# if the list is an empty list then how to add elements to it
# By using append() method we can add elements to the list
m.append(10) # In append method we can add only one element at a time
m.append(-20.5)
m.append("Sai Baba")
m.append(True)
m.append("Sai") # duplicate values are allowed in list
print(m)
print(m[0])
print(m[1])
m[1]=20.5 # list is mutable i.e if you use id to check memory location after every edit you will get same memory location.
print(m[1])
print(m)

# List is Mutable: we can change, add, remove elements after the list has been created.


# Indexing-> To acces single element from the list we use indexing
# Slicing-> To access multiple elements from the list we use slicing
print(m[-1]) # accessing last element
print(m[len(m)-1]) # accessing last element using len() function
print(m[3]) # accessing 4th element
res = m[2]
print(res)
print(res.count("a")) # count() method is used to count how many times a particular element is present in the list
print(m[2].count("a")) # count() method is used to count how many times a particular element is present in the list
print(m[2][4:8]) # accessing substring from the string present in the list
print(m[2][4:])
print(m[2][1])

m.insert(2,["Raj","Ravi"])# insert() method is used to add element at particular index
print(m)
monkey  = ['a','b','c','d','e','f','g','h','i']
print(monkey)
monkey.append('j') # append() method is used to add element at the end of the list


m[3] = "Gajanan Maharaj"
print(m)

# To print element of list which is itself a list for eg. if you have to print ravi and v of ravi
print(m[2][1]) # accessing ravi
print(m[2][1][2]) # accessing v of ravi
print(m[2][0][2]) # accessing j of raj 

chotu_list = ["Raj","my name is Rahul","Pavan",123,45.67,True]
var = chotu_list[1]
print(var.split()) # split() method is used to split the string into list of words
print(var.split()[3]) # accessing 4th word from the splitted list

# How to iterate a list using for loop
count = 1
for bj in chotu_list:
    print(f"Iteration {count}:",bj)
    count = count + 1
    
















#15-12-2025 :Monday
students_marks = [56,89,72,99,92,72,45,83,72,64,91,72]

#How to remove data from list
 
# Removing data using pop method, pop removes elemnent and returned value which is poped at that index & pop works with index
print(students_marks)
ele = students_marks.pop() # removes last element from the list
eles = students_marks.pop(3) # removes element at index 3
print(f"students_marks:{students_marks} & removed element is :{ele} & students_marks after removing index 3 element is :{eles} & students_marks now is :{students_marks}")
# print(students_marks.pop(20)) # IndexError: pop index out of range


# Removing data using remove method, remove method removes the first matching value but not returns the removed value & remove works with value
mes = students_marks.remove(72) # removes first matching value 72 & and it only removes first occurence of 72
print("Removed value:",mes) # Removed value: None bcoz remove method does not return any value
print("students_marks after removing 72:",students_marks)
#mess= students_marks.remove(100) # ValueError: list.remove(x): x not in list






