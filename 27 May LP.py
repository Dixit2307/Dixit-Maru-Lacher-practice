# LP 27 May

name="Dixit" 
age=18

print(name,age)
print(f"My name is {name} and I am {age} years old")

#Using.format()

print("My name is {} and I am {} years old".format(name,age))

# Using % formmating

print("My name is %s and I am %d years old"%(name,age))
print("\n")

#Price
price=199.456

print(f"price:{price:.2f}")

# list an tuple

# list

my_list=[18,45,63]

print("Original liat:",my_list)

my_list[1]=7
print("Modifide list:",my_list)

# Append()

my_list.append(50)
print("\nAfter append list:",my_list)

#remove()

my_list.remove(50)
print("\nAfter remove list:",my_list)

# Tuple

my_tuple=(100,200,300,400)
print("Tuple:",my_tuple)
print("\n")

Dix_tuple=(32,7,20,80)
print("My tuplr:",Dix_tuple)

# Access Element
print("\nFirst Tuple Element:",my_tuple)

# Indexing and Slicing

text="python"
words="Data analitics"

# Indexing

print("First latter:",text[0])
print("Last latter:", text[-1])
print("Last latter:",text[len(text)-1])

print("\nFirst latter:",words[0])
print("Last latter:", words[-1])
print("Last latter:",words[len(text)-1])

# slicing

print("\nFirst 3 latter:",text[:3])
print("First 3 latter:",words[:3])

print("\nLast 3 latter:",text[-3:])
print("\Last 3 latter:",text[3:])
print("Last 3 latter:",words[-3:])
print("Last 3 latter:",words[11:])

print("\nReverse String:",text[::-1])
print("Reverse String:",words[::-1])

students=["dixit","parth","rahul","prerna"]

print("\nOriginal list:",students)
print("First two student:",students[:2])

# loop

for student in students:
    print(f"welcome,{student}")

print("\n Length of list:",len(students))

print("Is parth present:","parth"in students)

#Nested list

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print("\n Matrix:",matrix)

# Accessing element

print("Middel Element:",matrix[1][1])

msg="Data analitics"

print("\nUppercase:",msg.upper)
print("capitalize:",msg.capitalize)
print("Replace:",msg.replace("analitics","sci"))
print("Split:",msg.split)

#



    


































