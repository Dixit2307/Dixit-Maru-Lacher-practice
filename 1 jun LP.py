# creat 1D array using loop

list_1 = [10,20,30,40,50]

for item in list_1:
    print(item)

list_2 = [12,19,16,18,15,25,35]
total=0

for item in list_2:
    total += item
    print(total)

print("Array of sum",sum(list_2))

# Write a program to find the length of a 1D array without using built-in function.

arr = []

size = int(input("Enter array size:"))

for item in range(size):
    value = int(input(f"a[{item}] = "))
    arr.append(value)

count = 0

for i in arr:
    count += 1

print("Length of array : " , count)

# Write a program to find average of a 1D array without using any built-in method.


arr = []

size = int(input("Enter array size:"))

for item in range(size):
    value = int(input(f"a[{item}] = "))
    arr.append(value)

sums = 0
count = 0

for i in arr:
    sums +=  i
    count += 1

average = sums / count

print("Average of array" , average)

# Print all even numbers from the array.

arr = []

size  = int(input("Enter size of array:"))

for i in range(size):
    value = int(input(f"a[{i}] = "))
    arr.append(value)

print("Even number:")

for i in arr:
    if i % 2 == 0:
        print(i)


print("Odd number:")

for i in arr:
    if i % 2 != 0:
        print(i)

# print First, Middel anf Last Element in array.

arr=[16,13,18,45,49,25,36]

print("First Element:",arr[0])
print("Last Element:",arr[-1])

middle=len(arr)//2

print("Middel Element:",arr[middle])


#Access Element in 2D Array.

#arr[row][column]

arr = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
]

print(arr[0][1])
print(arr[2][2])

# Take input in 2D array

arr = []

rows = int(input("Enter rows : "))
columns = int(input("Enter columns:"))

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"a[{i}][{j}]="))
        row.append(value)
    arr.append(row)

print(arr)

# Print 2D array using Nested Loop

arr = [
    [1,2],
    [3,4]
]

for i in arr:
    for j in i:
        print(j , end =" ")
        print()
























































































