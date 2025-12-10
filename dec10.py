s5 = "instagram and facebook"
s = "instagram"
s1 = s[0:5]

print("Result of s=",s)
print("Result of s[0:5]=",s[0:5])
print("Result of s[3:6]=",s[3:6])
print("Result of s[6:3]=",s[6:3]) # print("Result of s[6:3:1]=",s[6:3:1])  
print("Result of s[6:3:-1]=",s[6:3:-1])
print("Result of s[5:2:-1]=",s[5:2:-1])
print("Result of s[6:len(s)=",s[6:len(s)])
print("Result of s1=",s1)

print("Result of s5[10:13]=",s5[10:13])


print(s[-9:-4])

print(s[0:5:1])
print(s[0:5:2])


print(s[ : : 1])
print(s[ : :])
print(s[ : : +1])
print(s[0: : 1])
print(s[ : : -1])

# Iteration In Strings
for char in s:
    print(char)
    
# Find total number of "a" in string
count = 0
for ch in s:
    if ch == "a":
        count = count + 1
print("Total number of a in",s, " is",count)


for char in s[0:5]:
    print(char)