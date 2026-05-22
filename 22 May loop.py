# Break Statement

for i in range(1,7):
    if i == 5:
     break
    print(i)

# continu statment

for i in range(1,7):
    if i == 5:
     continue
    print(i)

# pass statment

for i in range(1,7):
    if i == 5:
        pass
    print(i)

# pattern in python

# right-angel Triangle

for i in range(1,6):
    for j in range(i):
     print("*",end="")
    print()

# number Triangle

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

# Inverted Triangle

for i in (6,5,4,3,2,1):
    for j in range(i):
      print("*",end=" ")
    print()

# pyramid pattern

row=5

for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")

for k in range(2*i-1):
     print("*",end=" ")
     print()

#Floyad's Triangle

num=1

for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

# else with loops

for i in range(5):
    print(i)
else:
    print("Loop Finished")

#break

for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("Lopp finished")

# list and Tuple

my_list=[10,20,30,50,70]
print("Origenal list",my_list)
my_list[0]=50
print("Modified List:",my_list)

# Tuple

my_tuple=(10,20,30)
print("tuple:", my_tuple)


















    


















