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

print(f"The uppercase of {g} is {g.upper()}") # Doing to uppercase using upper function
print(f"The lowercase of {g} is {g.lower()}") # Doing to lowercase using lower function
print(f"The titlecase of {g} is {g.title()}") # Doing to titlecase using title function
print(f"The casefold of {g} is {g.casefold()}") # Doing to casefold using casefold function
print(f"The capitalized of {g} is {g.capitalize()}") # Doing to capitalized using capitalize function
print(f"The swappedcase of {g} is {g.swapcase()}") # Doing to swappedcase using swapcase function
print(f"The startwith 'W' of {g} is {g.startswith('W')}")
print(f"The endswith 'y' of {g} is {g.endswith('y')}")

words = s.split(" ")
print(len(words)) 
print(words)

newstring = "#".join(words)
print(newstring)

s1 = "insta"
s2 = "gram"
s3 = s1 + s2
print(s3)
s4 = s1.join(s2)
print(s4)

s1.index("i")
s1.isalpha()
s1.isalnum()
s1.isdecimal()
s1.islower()
s1.isdigit()
s1.isidentifier()


countg = 0
spm = "Instagram"
# in operator
print("z" in "Python") #False
vowels = "aeiouAEIOU"
for ch in spm:
    if ch in vowels:
        countg = countg + 1
print(f"Total vowels in {spm} are {countg}")