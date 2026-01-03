# for printing square star pattern
for rows in range(5):
    for cols in range(5):
        print("*",end='')
    print()

print()
print()
print()


# for printing right angle triangle star pattern
N = eval(input("Enter the number of rows: "))
for rows in range(1,N+1):
    for cols in range(1,rows+1):
        print("*",end='')
    print()


print()
print()

# But it is wrong way to print , we have function just use it
def right_angle_triangle(N):
    for rows in range(1,N+1):
        for cols in range(1,rows+1):
            print("*",end='')
        print()
right_angle_triangle(N)


