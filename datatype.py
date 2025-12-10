# import keyword
# print(keyword.kwlist)

# INTEGERS
price = 120
print(type(price))
print(price)


# FLOATS
var = 20.5
f = -78.9
f2 = 10.0
print(type(var), type(f), type(f2))
print(id(var), id(f), id(f2))

# BOOLEAN
v1 = True #Internal value of True is 1
v3 = True
v2 = False # Internal value of False is 0
v4 = v1 + v2
print(v4, type(v4), id(v4))
print(v1, type(v1), id(v1))
print(v3, type(v3), id(v3))
print(v2, type(v2), id(v2))

#PRogram that accept integer,float and boolean data from terminal and  check data type of those value
d1 = int(input("Enter an integer value: "))
d2 = float(input("Enter a float value: "))
d3 = bool(input("Enter a boolean value: "))
# d1 = eval(input("Enter an integer value: "))
# d2 = eval(input("Enter a float value: "))
# d3 = eval(input("Enter a boolean value: "))
print(d1,"is",type(d1), d2,"is",type(d2), d3,"is",type(d3))


