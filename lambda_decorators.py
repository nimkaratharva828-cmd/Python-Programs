# def addTwo(a,b):
#     return a+b 
# Above function can be written using lambda as below
# Lambda functions are used when we need a nameless function for a short period of time.
lambda a , b : a + b
print((lambda a , b : a + b)(2,3))  # 5

fun = lambda a ,b : a - b
print(fun(7,2))  # 5

# Lambda functions are often used along with functions like map(), filter() and reduce().
test_marks=[45,67,89,23,12,78,90]

# Example of map() with lambda
grace_marks = list(map(lambda marks: marks + 5 , test_marks))
print("Grace marks using map and lambda:",grace_marks)  # [50, 72, 94, 28, 17, 83, 95]

# Example of filter() with lambda
even_marks = list(filter(lambda marks: marks % 2 == 0 , test_marks))
print("Even marks using filter and lambda:", even_marks) 

# Example of reduce() with lambda
from functools import reduce
maximum = reduce(lambda a, b: a if a > b else b, test_marks)
print("Maximum marks using reduce and lambda:", maximum) 
print()
print()


# Decorators
def displayName():
    print("Hello,Atharva")

def Mydecoration(fun):
    def wrapperFun():
        print("Good Morning!!!!!!!")
        print("*" * 20)
        fun()
        print("*" * 20)
        print("Bye Bye!!!!!!!")
    return wrapperFun
wrapperfun = Mydecoration(displayName)
wrapperfun()


print()
print()


# Another way to use decorators with @ symbol
# @Mydecoration
def displayName2():
    print("Python,Atharva")

def Mydecoration(fun):
    def wrapperFun():
        print("Good Morning!!!!!!!")
        print("*" * 20)
        fun()
        print("*" * 20)
        print("Bye Bye!!!!!!!")
    return wrapperFun
wrapperfun = Mydecoration(displayName2)
wrapperfun()
