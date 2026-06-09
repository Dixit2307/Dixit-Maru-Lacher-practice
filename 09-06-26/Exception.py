# Raise keyword

#Syntax

# raise Exception Type("Error Massage")

# Assert Keyword

# Syntax

# assert Condition ,"Error amessage"
'''
num=10
assert num > 0,"Number Must be Positive"

print("Valide number")

# Custome exception with try........except

class InsufficiantBalanceError(Exception):
    pass
balance=1000
withdraw=1500

try:
    if withdraw > balance:
        raise InsufficiantBalanceError('Not Enough Balance')
    print("Withdraw Succesfull !!")
except InsufficiantBalanceError as e:
    print("Error :",e)

#
num = int(input("Enter An Integer:"))

def check_even():



    if not isinstance(num , int):
        raise TypeError("Input Must Be An Integer")

    if num %2!=0:
        raise ValueError("Number is Odd")
        print("Number Is even")

try:
    check_even()

except ValueError:
    print("Enter Value Must be Number")

except Exception as e:
    print("Error:",e)
'''
# Student Grade Validation

class InvalidGradeValidation(Exception):
    pass

try:
    grade=int(input("Enter Grade:"))

    assert grade !="","Grade input Cannot"

    if grade < 0 or grade >100:
        raise ValueError("Grade Must Be Between 0 to 100")

    if grade < 40:
        raise InvalidGradeError("Student has Failed")
    print("Student Passed")

except AssertionError as e:
    print("Assertion Error",e)

except ValueError as e:
    print("Value error:",e)

except InvalidGradeError as e:
    print("Invalide Grade Error")






    

































    
