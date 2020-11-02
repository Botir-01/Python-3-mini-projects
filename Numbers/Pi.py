# =============================Numbers===========================
# Find PI to the Nth Digit
# Task: Enter a number and have the program to generate pi up to that many decimal places.
# Keep a limit to how far the program will go.

# we will calculate pi using Gregory-Leibniz series.

# importing the decimal module
from decimal import *

getcontext().prec = 150


# calculating pi using Gregory-Leibniz series.

def pi_generator(num):
    op = 1
    number = Decimal(4.0)
    result = Decimal(0.0)
    for n in range(1, 2 * num + 1, 2):
        result += number / (n * op)
        op *= -1
    return result


def ask():
    iteration = 0
    while True:
        try:
            iteration = int(input("How many repetitions? (Provide a large number for more concise result): "))
            break
        except:
            print("Please provide an integer value!")
            continue
    return pi_generator(iteration)


def main():
    user_input = 0
    pi = ask()
    while True:
        try:
            user_input = int(input("How many digits of pi's do you want to see?: "))
        except:
            print("Please provide an integer value!")
            continue
        else:
            break
    print("Your pi number is: {0:.{1}}".format(pi, user_input))


if __name__ == '__main__':
    main()
