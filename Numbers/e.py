# ===========================Numbers=====================
# Enter a number
# Have the program generate e up to that many decimal places
# Keep a limit to how far the program will go
from decimal import *

getcontext().prec = 150


# asking a user for the number of iteration that will go on.
def ask():
    iteration = 0
    while True:
        try:
            iteration = int(input('Enter a number higher than 100000 to iterate to: '))
            if iteration < 100000:
                print("Please provide a number higher than 100000")
                continue
        except:
            print('Ops, please provide an integer value!')
            continue
        else:
            break
    return iteration


# function to calculate e
def e_calc():
    number = Decimal(1.0)
    iteration = ask()
    result = Decimal((number + number / iteration) ** iteration)
    return result


def main():
    digits = 0
    calculation = e_calc()
    while True:
        try:
            digits = int(input('How many of e do you want to see: '))
        except:
            print('Please provide an integer value!')
            continue
        else:
            break
    print('Your e number is: {0:.{1}f}'.format(calculation, digits))


if __name__ == '__main__':
    main()
