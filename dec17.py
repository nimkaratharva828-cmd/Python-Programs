# Set and FrozenSet Operations--->Unordered |
#                                           |
#                                           V 
#                Indexing and Slicing is absent

s={}
print(type(s)) # By default {} is reserved for dictionary thus if we want to create emepty set we have to use set function.
p = set()
print(type(p))





# =========================
# SET IMPLEMENTATION
# =========================
# Creating a set
my_set = {1, 2, 3, 4}
print("Initial set:", my_set)

# Note: Sets do NOT allow duplicate values
dup_set = {1, 2, 2, 3}
print("Duplicates removed automatically:", dup_set)

# -----------------------------------
# Adding elements
# -----------------------------------

# add() → adds single element
my_set.add(5)
print("After add(5):", my_set)

# update() → adds multiple elements (list/tuple/set)
my_set.update([6, 7], (8, 9))
print("After update:", my_set)

# -----------------------------------
# Removing elements
# -----------------------------------

# remove() → removes element, error if not found
my_set.remove(3)
print("After remove(3):", my_set)

# discard() → removes element, NO error if not found
my_set.discard(100)
print("After discard(100):", my_set)

# pop() → removes random element
removed_item = my_set.pop()
print("Removed item using pop():", removed_item)
print("After pop():", my_set)

# clear() → removes all elements
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear():", temp_set)

# -----------------------------------
# Set Operations
# -----------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union → all unique elements
print("Union:", A | B)
print("Union using method:", A.union(B))

# Intersection → common elements
print("Intersection:", A & B)
print("Intersection using method:", A.intersection(B))

# Difference → elements in A not in B
print("Difference (A - B):", A - B)
print("Difference using method:", A.difference(B))

# Symmetric Difference → elements not common
print("Symmetric Difference:", A ^ B)
print("Using method:", A.symmetric_difference(B))

# -----------------------------------
# Set Comparisons
# -----------------------------------

C = {1, 2}
D = {1, 2, 3, 4}

# Subset
print("Is C subset of D?:", C.issubset(D))

# Superset
print("Is D superset of C?:", D.issuperset(C))

# Disjoint → no common elements
E = {10, 20}
print("Is C disjoint with E?:", C.isdisjoint(E))

# -----------------------------------
# Membership Testing
# -----------------------------------

print("Is 2 in A?:", 2 in A)
print("Is 10 not in A?:", 10 not in A)

# -----------------------------------
# Looping through set
# -----------------------------------

for item in A:
    print("Set element:", item)










# =========================
# FROZENSET IMPLEMENTATION
# =========================

# Creating a frozenset
fs = frozenset([1, 2, 3, 4])
print("Frozen set:", fs)

# Note: Frozen sets are IMMUTABLE (cannot change)

# ❌ These operations are NOT allowed
# fs.add(5)        # AttributeError
# fs.remove(2)     # AttributeError
# fs.pop()         # AttributeError

# -----------------------------------
# Frozen set operations (Allowed)
# -----------------------------------

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

# Union
print("Union:", fs1.union(fs2))

# Intersection
print("Intersection jhabbu:", fs1.intersection(fs2))

# Difference
print("Difference (fs1 - fs2):", fs1.difference(fs2))

# Symmetric Difference
print("Symmetric Difference:", fs1.symmetric_difference(fs2))

# -----------------------------------
# Comparisons
# -----------------------------------

print("Is fs1 subset of fs2?:", fs1.issubset(fs2))
print("Is fs1 superset of fs2?:", fs1.issuperset(fs2))

# -----------------------------------
# Membership testing
# -----------------------------------

print("Is 2 in fs1?:", 2 in fs1)

# -----------------------------------
# Using frozenset as dictionary key
# -----------------------------------

# frozenset can be used as key because it is immutable
my_dict = {
    frozenset([1, 2]): "Pair A",
    frozenset([3, 4]): "Pair B"
}

print("Dictionary with frozenset keys:", my_dict)

# -----------------------------------
# Looping
# -----------------------------------

for item in fs1:
    print("Frozen set element:", item)








# If a data type is mutable, it cannot be a dictionary key bcoz dictionary key must be IMMUTABLE.
