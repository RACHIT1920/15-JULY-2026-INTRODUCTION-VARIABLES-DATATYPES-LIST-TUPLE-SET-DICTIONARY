my_list=[1,2,3,4,5]
list1=[7,8,9]


# slicing
print(my_list[0:3])

# modification
my_list[0]=0;

print(my_list)

# append
my_list.append(6)

print(my_list)

# extend
my_list.extend(list1)
print(my_list)

# indexing
print(list1.index(7))

# count
print(list1.count(3))

# sort
print(list1.sort())

# reverse according to index
print(list1.reverse())


# tuple

tuple1={1,2}
tuple2={3,4}

# single item tuple
tuple3={1,}


print(tuple1)


one,two=tuple1

print(one)

# Dictionary

d={"abc":"Def",
   "qwer":"asdf"}


# d.items will convert dictionary into list and then we can iterate 
for k,v in d.items():  
    print(k,v)


# Set

s=set()


a={1,1,1,2,3,4}

print(a)


