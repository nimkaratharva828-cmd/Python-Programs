count = 0

s = "Wel come to Kiran Academy"
g = input("Enter any string to perform count operation:")
v = input("Enter any character to find it's count:")

for geg in g:
    if geg == v:
        count = count + 1
print(f"There are total {count} {v} in {g}")
print(f"The length of {g} is {len(g)}")

# You can do all these magajmari in one function of python named as Count function
cnt = g.count(v)
print(f"The count of {v} using count function is {cnt}")

