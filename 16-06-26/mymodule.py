# Creating , Importing &  Renaming Modules
#__name__ with __main__
# Creating & using package
# dir() and __init__.py

'''
A Module is a python file that containes functions , Variables or 
classes whice can be reused in another programe.
'''

# 1. Creating a Module

def prints(name):
    print("Name :",name)
    
def add(a,b):
    print(a + b)
    print(a * b)
    print(a - b)
    print(a // b)

# 2. Creat __name__ with __main__

# Every python file has a special variable caller __name__.

#Syntax 
#__name__ == module_name

#This is used to control which code should run directly

# 3. Creating & using packages defination 

# 4.dir() function

'''
 dir() is a bilt in function used to display a properties , method
 and functions of an object or module. 
'''

import math
print(dir(math))

# 5. __init__.py

'''
__init__.py is a special file used to make a folder as a python 
packge it can also contain initialization code for the packge
'''

# use as renaming

 







