# multilevel inheritance

class GrandParent:
    def m1(self):
        print("Grand Parent Class")
class Parent(GrandParent):
    def m2(self):
        print("Parent Class")
class Child(Parent):
    def m3(self):
        print("Child Class")

c1=Child()
c1.m1() 
c1.m2()
c1.m3()
  
print()
print()
print()

# Hierarchical Inheritance
class parent:
    def method1(self):
        print("inside method1 of parent class")
class child_1(parent):
        def method2(self):
            print("inside method2 of child class")
class child_2(parent):
    def method3(self):
        print("inside method3 of child2 class")

jay= child_1()
jay.method1()
jay.method2()

viru= child_2()
viru.method1()
viru.method3()

print()
print()
print()

# Multiple Inheritance
class Father:
    def m1(self):
        print("Father Class")
class Mother:
    def m2(self):
        print("Mother Class")
class Child(Father,Mother):
    def m3(self):
        print("Child Class")
c1 = Child()
c1.m1()
c1.m2()
c1.m3()

print()
# if we have same method in both parent class then the method of first parent class will be called
# MRO - Method Resolution Order - it tells the order in which methods are inherited from parent classes
# and MRO reduces ambiguity or no diamond problem in python
class Father1:
    def m1(self):
        print("Father1 Class")
class Mother1:
    def m1(self):
        print("Mother1 Class")
class Child1(Father1,Mother1):
    def m2(self):
        print("Child1 Class")
c2 = Child1()
c2.m1()
c2.m2()
print(Child1.__mro__) # it shows the order in which methods are inherited from parent classes