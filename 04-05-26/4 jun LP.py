#Abstraction in OOP
'''
#1. abc(Absract Base Class)

from abc import ABC,abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Boww Boww.")

d=Dog()
d.sound()
'''
# Abstract Class and Method

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound (self):
        pass
    def sleep(self):
        print("Animal is sleeping")
#child calss

class Dog(Animal):
    def sound(self):
        print("Dog boww boww")

class Cat(Animal):
    def sound(self):
        print("Cat Meow meow...")

d=Dog()
d.sound()
d.sleep()

c=Cat()
c.sound()
c.sleep()

#Lab Work
# Abstract class shape with area()

from abc import ABC,abstractmethod
class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

class Circle(shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius


r=Rectangle(9,4)
c=Circle(11)

print("Rectangle Area:",r.area())
print("Circle Area:",c.area())

# MLModel Abstract Class

from abc import ABC,abstractmethod

class MLModel(ABC):

    @abstractmethod
    def train(self):
        pass
    @abstractmethod
    def predict(self):
        pass

# Linear Regression Model

class LinearRegressionModel(MLModel):
    def train(self):
        print("Training Linear Regression Model")

    def predict(self):
        print("Predicting Using Linear Regression")

class DecisionTreeModel(MLModel):
    def train(self):
        print("Training Decision Tree Model")

    def predict(self):
        print("Pridicting Using Decision Tree Model")

l=LinearRegressionModel()
d=DecisionTreeModel()

l.train()
l.predict()

d.train()
d.predict()
    
    















































































































































































































































