class Student():

    # Constructor with self keyword
    def __init__(self,r,n,c,s):
        self.roll = r
        self.name = n
        self.city = c
        self.subject = s

s1 = Student(101,"Rahul","Delhi","Python")
print(f"Student name is {s1.name} Roll No. is: {s1.roll}")


s2 = Student(102,"Sonam","Mumbai","Java")
print(f"Student name is {s2.name} Roll No. is: {s2.roll}")

