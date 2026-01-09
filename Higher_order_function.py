test_marks = [10,30,65,25,89,64,85,565,55]
grace_marks=[]


# OLD MEthod without higher order function
# for i in test_marks:
#     grace_marks.append(i+5)
# print("Original Marks:", test_marks)
# print("Marks after adding grace marks:", grace_marks)


# Using higher order function
def addFive(n1):
    return n1+5

# Using higher order function without map()
for i in test_marks:
    m = addFive(i)
    grace_marks.append(m)
print("Original Marks:", test_marks)
print("Marks after adding grace marks using function:", grace_marks)


# Using map() higher order function
new_grace_marks = list(map(addFive, test_marks))
print("Marks after adding grace marks using map():", new_grace_marks)

print()
print()


# Using Filter higher order function
test_marks2=[10,30,65,25,89,64,85,565,55]
topper_list=[]
def topper(marks):
    return marks>85
topper_list = list(filter(topper, test_marks2))
print("Original Marks:", test_marks2)
print("Topper Marks using filter():", topper_list)

print()
print()
# Using Reduce higher order function


from functools import reduce
test_marks3=[10,30,65,25,89,64,85,55]
def addTwo(a,b):
    return a+b
def max(a,b):
    if a>b:
        return a
    else:
        return b
total_marks = reduce(addTwo, test_marks3)
max_num = reduce(max, test_marks3)
print("Original Marks:", test_marks3)
print("Total Marks using reduce():", total_marks)
print("Maximum Marks using reduce():", max_num)
