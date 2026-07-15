name="qwertyuiop"
print(len(name))
print(name[4])

print(name[0:5])

# negative indexing
print(name[-1])

# Skipping characters

print(name[0:4:2])

# reverse string

print(name[::-1])

#string operations

name1="asdfg  "

print(name+name1)

# repetition
print(name1*3)


# find in string membership operator

print("q" in name)

# methods in string

print(name.upper())
# remove trailing and leading whitespaces
print(name1.strip())

print(name.find('q'))

print(name.count('s'))