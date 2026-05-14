

x=10
y=12

print(id(x))
print(id(y))

# int

x=13
print("Before:",id(x))
x=x+1
print("After:",id(x))

y=12
print("Before:",id(y))
y=y+34
print("After:",id(y))

numbers=[1,2,3,4,5]

print("Before:",numbers)
print("Before:",id(numbers))
 
numbers.append(4)

print("after:",numbers)
print("after:",id(numbers))


numbers.append(6)

print("after 2:",numbers)
print("after 2:",id(numbers))

 
# Multipul dictionary

student={"name":"dixit",
     "Age":17}
print(student)

student["age"]=18
print(student)

# string

d_str=" Hello python"
print(d_str)

print(d_str[0])
print(d_str[5])
print(d_str[0:6])


 

