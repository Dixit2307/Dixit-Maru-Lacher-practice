# Python Modules & Functions

# 1. MATH Module

print("\n === Math Module ===")

import math

#1. sqrt()

number = 121

result = math.sqrt(number)

print("Square Root of" , number , " = " , result)

#2. pow()

base = 2
power = 5

result = math.pow(base , power)

print(base , "power" , "=" , result)

# 3. ceil()

number = 4.9
result = math.ceil(number)

print(result)

# 4. floor()

number = 4.1

result = math.floor(number)

print(result)

# 5. factorial()

number = 10

result = math.factorial(number)

print(result)

# 6. gcd()


num1 = 12
num2 = 18

result = math.gcd(num1 , num2)

print(result)

# 7. sin()

result = math.sin(0)

print(result)

#8. cos()

result = math.cos(0)

print(result)

# 9. tan()

result = math.tan(1)

print(result)

# 10. log()

number = 10

result = math.log(number)

print(result)

# 11. pi

print(math.pi)

# 12. e

print(math.e)

# 2. RANDOM Module #

import random

print("\n === Random Module ===")

#1. randint()

result = random.randint(1 , 10)

print(result)

#2. random()

result = random.random()
print(math.floor(result * 10000))

#3. choice()

colors = ["Blue" , "Orange" , "Red" , "Yellow"]

result = random.choice(colors)

print(result)

# 4. shuffle()

numbers = [1 , 2 , 3 , 4 , 5 , 6]

print(numbers)

random.shuffle(numbers)

print(numbers)

# 5. uniform()

result = random.uniform(1 , 100)

print(result)

# 6. randrange()

result = random.randrange(1 , 20 , 2)

print(result)

# 7. sample()

numbers = [10 , 20 , 30 , 40]

result = random.sample(numbers , 2)

print(result)

# 3. UUID module

# uuid.uuid1()

print("\n === UUID Module ===")
import uuid

result = uuid.uuid1()

print(result)

# uuid4()
result = uuid.uuid4()

print(result)

# uuid3()

result = uuid.uuid3(uuid.NAMESPACE_DNS , "example.com")

print(result)

# uuid5()

result = uuid.uuid5(uuid.NAMESPACE_DNS , "example.com")

print(result)
