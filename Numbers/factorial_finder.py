# =================================Numbers=============================
# The factorial of a positive integer n is defined as the product of the sequence , n-1, n-2, ...1
# and the factorial of 0 is defined as being 1.
# Solve this using both loops and recursion.
import math


# with while loop

def with_while(num):
    minus = num
    oper = 1
    var_num = num
    while var_num > 1:
        num *= (minus - oper)
        oper += 1
        var_num -= 1
    return num


# with for loop
def with_for(num):
    for i in range(1, num):
        num *= i
    return num


def with_recursion(num):
    return num * math.factorial(num - 1)


def main():
    user_input = 0
    while True:
        try:
            user_input = int(input('Enter a positive value to find its factorial: '))
        except ValueError:
            print('Please provide appropriate numbers!')
            continue
        else:
            break
    if user_input < 0:
        return print("Sorry, factorial does not exist for negative numbers!")
    elif user_input == 0:
        return print(f'The factorial of {user_input} is 1')
    while True:
        user_choice = input('What method would you like to use: \n'
                            '1: while loop \n'
                            '2: for loop \n'
                            '3: recursion: ')
        if user_choice == '1':
            answer = with_while(user_input)
            return print(f'The factorial of {user_input} is {answer}')
        elif user_choice == '2':
            answer = with_for(user_input)
            return print(f'The factorial of {user_input} is {answer}')
        elif user_choice == '3':
            answer = with_recursion(user_input)
            return print(f'The factorial of {user_input} is {answer}')
        else:
            print('Please choose from one of the provided options!')
            continue


if __name__ == '__main__':
    main()
