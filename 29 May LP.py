# 29 May LP

def multi(a,b):
    print("Multiplication:",a*b)

multi(12,7)

#
def factorial(n):

    if (n==1):
        return 1
    return n*factorial(n-1)
print(factorial(5))

#
def total(n):
    if n==0:
        return 0
    return n + total(n-1)
print(total(5))

#
square = lambda x:x*x
print(square(5))
add = lambda a,b : a+b
print(add(10,20))

#list

numbers=[1,2,3,4,5,6,7,8,9,10]

result= list(map(lambda x:x*2, numbers))
print(result)

#Filter

numbers=[1,2,3,4,5,6,7]

odd=list(filter(lambda x:x%2!=0,numbers))
print(odd)

x=100
def show():
    print(x)

count=0

def increment():
    global count
    count += 1

increment()
increment()
increment()

print(count)

def calculation(a,b):
    return a+b,a-b

result=calculation(15,9)
print(result)

def student():
    name="Dixit"
    marks=90

    return name,marks
n,m=student()

print(n)
print(m)
numbers=[1,2,3,4,5,6,7]

print("Length:",len(numbers))
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))

print("\n")

def greet(name):
    return "Hello"+name

print(greet(" student"))

def add_number(*args):
    total =0
    for num in args:
        total += num
    return total
print(add_number(1,2,3,4,5,6))
'''
def student_info(**kwargs):
    for keyvalue in kwargs.items():
     print(key,":",value)

student_info( name = "Rahul",age=20)
'''
def multiply(a,b):
    """This function returns the multiplication of two numbers"""
    return a*b

print(multiply(9,6))
print(multiply.__doc__)

def greet():
    print("Hello, Python Students")

greet()

def add(a,b):
    print("Addition:",a+b)

add(23,54)

print("\n")
def message():
    return "Hello Students"

print(message)

def multiply(a,b):
    return a*b
result=multiply(4,8)
print(result)
    







































































