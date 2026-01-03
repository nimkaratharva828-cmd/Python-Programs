def add_two(p1,p2):
    res = p1 + p2

op = add_two(30, 10)
print(op) # Function will return none bcoz we not write return in that function
print(f"Result type: {type(op)}")


print()
print()
print()
print()
print()
print()


def addd_two(p3,p4):
    resu = p3,p4
    return resu
op = addd_two(30, 10)
print(op)






print()
print()
print()
print()
print()

def atharva(n1, n2, n3):
    result= n1 + n2 + n3
    subtract= n1 - n2 - n3
    return result,subtract

def nimkar(n1,n2,n3):
    # return n1 + n2 + n3
    # return n1 - n2 - n3  # A function cannot execute "two return" statements one after another
    return n1 + n2 + n3, n1 - n2 - n3
    
n1 = eval(input("Enter 1st No. :"))
n2 = eval(input("Enter 2nt No. :"))
n3 = eval(input("Enter 3rt No. :"))
# op = atharva(n1, n2, n3)
#print(op)
print(atharva(n1, n2, n3))
print(nimkar(n1, n2, n3))
