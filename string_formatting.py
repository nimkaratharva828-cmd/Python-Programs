#String formatting can done using following methods :
# 1.Format method
# 2.f" ":-> f string way
# 3.%s,%d


#Format Method
age = 21
name = "Raj"
city = "Wardha"

s = "Student name is {} and age is {} lives in {}.".format(name,age,city)  # {} is placeholder and .format(name,age) is a method of formatting
s2 = "Student name is {n} and age is {a} lives in {c}.".format(c = city ,a = age, n = name,) 
print(s)
print(s2)


# Old way using % operator

s3 = "Student name is %s and age is %d lives in %s." %(name,age,city)
print(s3)


# f" " :-> (Python 3.6+)
s4 = f"Student name is {name} and age is {age} lives in {city}."
print(s4)

# Table creation using f-strings

r = "Roll No"
n = "Name"
m = "Marks"

r1 = 1
n1 = "Jay"
m1 = 90
r2 = 2
n2 = "Shah"
m2 = 10

print("-"*44)
print(f"|{r:^10}|{n:^20}|{m:^10}|")
print("-"*44)
print(f"|{r1:<10}|{n1:^20}|{m1:^10}|")
print("-"*44)
print(f"|{r2:>10}|{n2:^20}|{m2:^10}|")
print("-"*44)
