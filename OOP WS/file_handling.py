# Read the entire file
f = open('file_handling.txt', 'r')
print(f.read())
f.close()

print()
print()

# Read the file line by line
f = open('file_handling.txt', 'r')
for line in f:
    print(line.strip())
f.close()

print()
print()

# Append to the file
f = open('file_handling.txt', 'a')
f.write('This is an appended line.')
f.close()
f = open('file_handling.txt', 'r')
print(f.read())
f.close()

