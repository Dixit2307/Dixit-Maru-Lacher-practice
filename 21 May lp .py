# Simple Calculater
num1=50
num2=45

operator="+"

match operator:
    case "+":
           print("Addition=",num1+num2)
    case "-":
        print("substraction=",num1-num2)
    case "*":
        print("Multipication=",num1*num2)
    case "/":
        print("Division=",num1/num2)
    case _:
        print("invalid operator")

#while loop

i=1
while i<=5:
      print(i)
      i+=1

#For loop

#Print number 1 to 5

for i in range(1,6):
    print(i)

# loop with string

name="python"
for i in name:
    print(i)

# Loop with list

fruits=["Apple","Banana","Mango","Orange"]

for item in fruits:
     print(item)

# Range Function

for i in range(5):
    print(i)

for i in range(1,10):
    print(i)

for i in range(0,10,2):
    print(i)

#Nested loop

for i in range(1,18):
    for j in range(1,9):
        print(j,end="")
        print()

for i in range(1,6):
    for j in range(1,11):
        print(j,end="")
        print()














































      



    
