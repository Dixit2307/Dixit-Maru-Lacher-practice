

def check_even():

    num = int(input("Enter An Integer:"))

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