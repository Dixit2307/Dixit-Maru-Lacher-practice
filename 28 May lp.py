# CRUD Operation in python

#C:Create
#R:Read
#U:Update
#D:Delete

# Empty List

students=[]

# CREATE

student1={
    'id':1,
    'name':'Tushar',
    'email':'tushar@gmail.com'
    }

student2={
    'id':2,
    'name':'Hitesh',
    'email':'hitash@gmail.com'
    }

student3={
    'id':3,
    'name':'jay',
    'email':'kjay@gmail.com'
    }

# Add User

students.append(student1)
students.append(student2)
students.append(student3)

print("User Added Successfully !")
print("\n")


# READ

print("\nAll students:")

for student in students:
    print(student)

# SEARCH

search_id=2

print("\n Searching User:")

for student in students:

    if student['id']==search_id:
        print("User Found:",student)

#UPDATE

print("\n Updating User Email....")

for student in students:

    if student['id']==2:
        student['email']='hitash@yahoo.com'
print("User Updated!")
print(students)

# DELETE

print("\n Deleting student")

for student in students:
    if student['id']==1:
        students.remove(student)
        break

print("Student Deleted")
print(students)

# Count Students

print("\n Total Users:",len(students))

#Chack Email Exists

check_email='kjay@gmail.com'
found =True

if student['email']==check_email:
    found=True

if found :
    print("Email Exists")
else:
    print("Email not Exists")

# Sort by student name.

sorted_students=sorted(students,key=lambda x:x['name'])

print("\n Sorted Students:")

for student in sorted_students:
    print(student)

# Final User List

print("\n ============== Final Students ==============")

for student in students:
    print(f'''
ID:{student['id']}
Name:{student['name']}
Email:{student['email']}
''')

# type casting Constructor

# List()

a=[1,2,3,4]
b=tuple(a)
c=set(a)

print(a)
print(b)
print(c)

# del Keyword

x=[10,20,30,40]
print(x)

del x[1]
print(x)

person={'name':'Jay','age':18}

del person['age']

print (person)

del(x)

print(x)








































