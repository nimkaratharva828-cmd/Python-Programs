class Student:
    c_name = "TKA" # Class Variable

    def __init__(self, r, n, m):
        self.roll = r
        self.name = n
        self.marks = m

    # Instance Method
    def displayAllDetails(self):
        print(f"Name: {self.name}")
        print(f"College: {self.c_name}")

    # def updateMarks(self, new_marks):
    #     self.marks = new_marks

    # Class Method
    @classmethod
    def displayCollegeName(cls):
        print(f"College Name: {cls.c_name}")







s1 = Student(101, "Rahul", 95)
s2 = Student(102, "Anjali", 88)

s1.displayAllDetails()
# s1.updateMarks(980)
s1.displayAllDetails()
s2.displayAllDetails()



