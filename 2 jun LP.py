# 1. Find seconde Largest Elements

arr=[45,7,18,63]
arr.sort()

print(arr)
print("Second Largest:",arr[-2])

#2. Remove Duplicate Elements

arr=[11,22,33,44,22,11,33,66]

unique=[]

for i in arr:
    if i not in unique:
        unique.append(i)
print("Array:",unique)

#3. Frequency Of Each Element

arr=[1,2,3,4,5,6,6,2,5,3,2,5]

for i in set(arr):
    print(i,"Appears",arr.count(i),"Times")

#4. Find Missing Number

arr=[1,2,3,4,5,6,7,8,9,10]

n=10

expected=n*(n+1)//2

actual=sum(arr)

print("Missing Number",expected-actual)

# Merge and sort Two arrays

arr1=[60,30,10]
arr2=[20,40,50]

marged= arr1 + arr2

print(marged)

marged.sort()
print(marged)

# Kadane's Algoritham

arr=[-2,1,9,-5,6,3,-2,7]

current=maximum=arr[0]

for i in arr[1:]:
    current=max(i,current+i)
    maximum=max(maximum,current)

print("Maximum Sum",maximum)

#2D Array

#Addtion of Two Matrix

A=[
    [1,2],
    [3,4]
    ]

B=[
    [5,6],
    [7,8]
    ]

result=[]

for i in range(len(A)):
    row=[]
    for j in range(len(A[0])):
        row.append(A[i][j]+B[i][j])

    result.append(row)
for row in result:
    print(row)


# Find Largest Element in each row

matrix=[
    [12,32,54],
    [65,45,98],
    [78,89,23]
    ]

for row in matrix:
    print("Largest:",max(row))















