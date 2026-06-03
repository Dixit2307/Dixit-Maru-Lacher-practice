# 3 Jun LP

#1. Class and Object

# Faculty Class
'''
class Faculty:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating Object

f1=Faculty("Vivek sir",26)
f2=Faculty("Zeel sir",26)

f1.Display()
f2.Display()

# stdents class

class students:
    def __init__(self,name,caurse):
        self.name=name
        self.caurse=caurse
    def show(self):
        print("Student Name:",self.name)
        print("Student's Caurse:",self.caurse)
s1=students("Jay","Ethical hacking")
s1.show()

# del

class student:
    def __init__(self):
        self.name="Jay"
s1=student()
print(s1.name)
del(s1.name)



#1. Encapsulation


class bankaccount:

    def __init__(self):
        self.__balance=100000
    def deposit(self,amount):
        self.__balance += amount
    def withdrew(self,amount):
        self.__balance -+ amount
    def get_balance(self):
        return self.__balance
acc1=bankaccount()
acc1.deposit(30000)

print("Account Balance:",acc1.get_balance())

#2. polimorphisam

# Method Overriding

class Animal:
    def sound(self):
        print("Animal Makes Sound")

class Cat:
    def sound(delf):
        print("Cat MEOOWw MEOOWW....")
class Dog:
    def sound(self):
        print("Dog Boww boww")
c=Cat()
d=Dog()
c.sound()
d.sound()

# Same function Diffrent Objects

class car:
    def move(self):
        print("Car is running")
class plane:
    def move(self):
        print("Plane is Flying")

def action(vehical):
    vehical.move()

c=car()
p=plane()

action(c)
action(p)

# Abstraction

# Vehical

class vehical():
    def start(self):
        pass
class car(vehical):
    def start(self):
        print("Car started")
class bike(vehical):
    def start(self):
        print("Bike started")

c=car()
b=bike()

c.start()
b.start()

'''
'''
#4.Inharitance

# Single

class parent:
    def show(self):
        print("Parent Class")
class child(parent):
    pass

c=child()
c.show()

# Multilevel Inheritance

class Grande_parent:
    def tital(self):
        print("Grande Parent")

class parent (Grande_parent):
    def tital1(self):
        print("Parent")
class child (parent):
    def tital2(self):
        print("child")
obj=child()

obj.tital()
obj.tital1()
obj.tital2()

# Multiple Inheritance

class father:
    def father_property(self):
        print("Car")

class mother:
    def mother_property(self):
        print("jewellry")

class child(father,mother):
    pass

c=child()

c.father_property()
c.mother_property()

#4. Hierarchical 

class parent:
    def display(self):
        print("parent Class")

class child1(parent):
    pass
class child2(parent):
    pass

c1=child1()
c2=child2()

c1.display()
c2.display()
'''
#5.Hibrid inheritance

class A:
    def showA (self):
        print("A Class")

class B(A):
    def showB(self):
        print("B Class")

class C(A):
    def showC(self):
        print("C Class")

class D(B,C):
    def showD (self):
        print("D Class")

obj=D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()























































































