# Exception Hendeling in python.

'''
try
catch
else
finally
'''

# 1.try..........except.

try:
    num=int(input("Enter Number"))
    print(10/num)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Invalid Input")


# 2.try........except...........else

try:
    num=int(input("Enter Number"))
    result=10/num
except ZeroDivisionError:
    print("annot Divide by Zero")
else:
    print("Result:",result)


# 3.try........except.........finally

try:
    file=open("demo.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Programe Finished")


# 4. try.......except........else.........finally

try:
    num=int(input("Enter Number"))
    result=10/num
except ZeroDivisionError:
    print("Cannnot divide by zero")
else:
    print("Result",result)
finally:
    print("Programe Finished")

try:
    ATM_PIN=int(input("Enter ATM PIN:"))

except ValueError:
    print("PIN Must contain Numbers Only")

else:
    print("Pin Accepted")
    
    


