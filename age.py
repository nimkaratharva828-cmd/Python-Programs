# r = int(input("Enter your age: "))
# if r >= 18 :
#     print("Age is : ",r,"and he is Adult")
# else:
#     print("Age is :",r,"and he is Minor")

age = input("Enter your age:")
name = input("Enter your Name:")
print(type(age))
print(type(name))
print(id(age))
print(id(name))
print("User's age is:",age)
print("User's Name is:",name)
age = int(age)
if age >= 18 :
    print(name,"'s age is:",age,"and",name,"is Adult")
else:
    print(name,"'s age is:",age,"and",name," is Minor")