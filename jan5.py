def sign_up(en,age,sal,cn):
    print(f"Name of Employee is: {en}")
    print(f"Age of Employee is: {age}")
    print(f"Salary of Employee is: {sal}")
    print(f"Company Name is: {cn}")


#Positional Argument :- If you change the position of arguments then the output will be wrong. 
sign_up(24,25000,"TCS","Jay")
sign_up("Jay",24,25000,"TCS")

print()
print()
print()
print()

# Keyword Argument :- If you use keyword argument then the position of arguments does not matter.
sign_up(cn="TCS",sal=25000,en="Jay",age=24)
print()
print()
sign_up(sal=60000,age=21,cn="Google",en="Aryan")

print()
print()
print()
print()

# Default Argument :- If you do not pass any value to the argument then the default value will be taken.
# Default Argument must be written in last.
# Normal Argument must written before any Default Argument.
def sign_upd(en,age,sal,cn="TCS"):
    print(f"Name of Employee is: {en}")
    print(f"Age of Employee is: {age}")
    print(f"Salary of Employee is: {sal}")
    print(f"Company Name is: {cn}",end="\n\n")
    
sign_upd(age=25,sal=30000,en="Karan")
sign_upd(age=25,sal=30000,en="Mangesh",cn="Infosys")
sign_upd(age=25,sal=30000,en="Kamra")

# Arbitrary Argument :- If you do not know how many arguments will be passed in the function then use arbitrary argument.
# Arbitrary Argument is also called as Variable Length Argument.
# Positional Arbitrary Argument
def add(n1,n2):
    s = n1 + n2
    return s
# add(10) # here will give error because 2 arguments are required.
s = add(n2=30,n1=22)
print(s)
print()
print()
# But if we want to pass multiple arguments that we don't know then above function will not work.
def adds(*args):
    print(args)
    print(type(args))
    return s
adds(10,30)
adds(10,20,30,40,50)
adds(1,2,3,4,5,6,7,8,9,10)

print()
print()

def addss(*args):
    print(args)
    print(type(args))
    sum = 0
    for i in args:
        sum+=i
    return sum
res=adds(30,10)
print(res)
res=adds(10,30)  # Position matter , thus it is positional arbitrary argument
print(res)
res=addss(10,20,30,40,50)
print(res)
res=addss(1,2,3,4,5,6,7,8,9,10)
print(res)


print()
print()


# Keyword Arbitrary Argument
def submit(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # for t in kwargs.items(): # this will give tuple of key and value
    #     k,v =t               # Items method returns key-value pairs as tuples
    #     print(t)
    #     print(type(t))

    for k,v in kwargs.items():
        print(k)
        print(type(k))
        print(v)
        print(type(v))


submit(name="Jay",mobile=1234567890,age=24)
submit(course="Python",duration="2 months",price=2000)
submit(cn="TCS",sal=25000,en="Jay",age=24)