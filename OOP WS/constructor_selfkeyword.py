class Student():
    def __init__(self,r,n,c,s):
        self.roll = r
        self.name = n
        self.city = c
        self.subject = s

s1 = Student()
print(s1)
print(type(s1))



print(f"Student Roll: {s1.roll} and Name: {s1.name}")

