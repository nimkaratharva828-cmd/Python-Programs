#Input Function

sub1 = input("Enter marks of sub1: ")
sub2 = input("Enter marks of sub2: ")
sub3 = input("Enter marks of sub3: ")


print(type(sub1))

sub1 = int(sub1 )
sub2 = int(sub2 )
sub3 = int(sub3 )

sub4 = int(input("Enter marks of sub4: "))
sub5 = int(input("Enter marks of sub5: "))


total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total/500)*100

print("Total Marks: ", total)
print("Percentage is: ",percentage)