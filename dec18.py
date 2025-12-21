# Dictionary Operations
# Dictionary is unordered but in versions of python above 3.5 provides ordered feature to maintain data guarantee. 
# Key must be Immutable but value can be Mutable.

gfg = {"a":"snake",9:"mama",8:True,5:{},"m":(87,64)}
print(gfg)
print(type(gfg))
print(type(gfg["m"]))
print(type(gfg[5]))
print(gfg["a"])
print(gfg[9])





# Level 1 : Dictionary
# Create dict of IPL Players with Jersey no. and name of Players
mi = {
    45: "Rohit Sharma",
    33: "Hardik Pandya",
    93: "Jasprit Bumrah",
    63: "Suryakumar Yadav",
    9: "Ishan Kishan",
    55: "Tilak Varma",
    27: "Kieron Pollard",
    23: "Piyush Chawla",
    4: "Tim David",
    12: "Dewald Brevis",
    5: "Jason Behrendorff",
    15: "Arjun Tendulkar",
    24: "Cameron Green",
    17: "Akash Madhwal"
    }

# How to access data drom dict ?----> By using key
print(mi[45])
mi[45] = "M.S.Dhoni" # It will not print "M.S.Dhoni" as duplicate keys are not allowed in dict....if you do it over_rides "M.S.Dhoni"  
mi[7] = "M.S.Dhoni"
print(mi[7])

# Iterate dict
for i in mi:
    print(i)  # It will print keys but not values

for ke in mi:
    print(mi[ke]) # It print Values

for g in mi:  # Here we want both key and values thus we need to do this but instead of this we have items() method which we learn in dec19.py
    print(g,"------->",mi[g]) # It print key and value



# Level 1.5 : Dictionary
# Find total players in team
print(f"Total players in Mi Team : {len(mi)} with jersey no.")
for lop in mi:
    print(lop)

# Display player names from mi team who contains "Y" in their name.
print("Player names with y in their names are :")
count = 0
for mg in mi:  # Since values are string it means all methods and function of strings can applied here
    if "y" in mi[mg]: 
        print(mi[mg])
        count = count + 1
print(mi[mg],"\nTotal players having y in their names are :",count)

# Display name of players having size of name above 12 characters
ct = 0 
for gfg in mi:
    if len(mi[gfg]) > 12:   # if mi[gfg] > 12:Not possible bcoz names are string and 12 is int
        print(mi[gfg])
        ct = ct +1 
print("Total players with name size more than 12:",ct)

# Display every character from mi players name whose name ends with "a"
print("\n\nNames of MI players whose names end with 'a':")
for lop in mi:
    if mi[lop].endswith("a"):
        print(mi[lop])   # Print names of MI players whose names end with "a"


print("\nCharacters of MI player names whose names end with 'a':")
for lop in mi:
    if mi[lop].endswith("a"):
        for ch in mi[lop]:
            print(ch) # Print every character of MI player names that end with "a"

