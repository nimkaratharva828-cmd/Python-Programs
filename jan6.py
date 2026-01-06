# Write a programme to find factorial of 5
def fact(N):
    print(f"Computing factorial of {N}")
    if N==1:
        return N
    return N * fact(N-1)

a = eval(input("Enter a number to find factorial: "))
res = fact(a)
print("Factorial of", a, "is", res)
print()
print()
# Nested Function
# Syntax for nested function
# def outerFun():
#     def innerFun():
#         pass
#     innerFun()
# outerFun()

def outerFun(X):
    print("This is outer function")
    print(X)
    def innerFun():
        print("This is inner function")
        print(X)
    print("Calling inner function")
    innerFun()
outerFun(10)

print()
print()


# Closure Function :-> A nested function used to data hiding
def outerfun(a):
    def innerfun(b):
        return a+b
    return innerfun  # Here we not type () after innerfun bcoz we want to return definition of innerfun and not function call
fun = outerfun(10) # here 10 is hidden value of a
res = fun(20) # 20 + 10 = 30
print("Result is:", res) 
res2 = fun(35) # 35 + 10 = 45
print("Result2 is:", res2)