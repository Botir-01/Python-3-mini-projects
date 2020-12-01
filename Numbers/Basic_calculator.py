# ====================================Numbers======================================
# Calculator - A simple calculator to do basic operators.


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiple(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def main():
    first_number = 0
    second_number = 0
    answer = 0
    while True:
        try:
            first_number = float(input("Enter the first number: "))
        except:
            print('Please enter some value!')
            continue
        else:
            break
    while True:
        try:
            second_number = float(input("Enter the second number: "))
        except:
            print('Please enter some value!')
            continue
        else:
            break
    while True:
        user_choice = input('Choose from one of these available operations (+, -, /, *): ')
        if user_choice == '+':
            answer = add(first_number, second_number)
            break
        elif user_choice == '-':
            answer = sub(first_number, second_number)
            break
        elif user_choice == '/':
            answer = division(first_number, second_number)
            break
        elif user_choice == '*':
            answer = multiple(first_number, second_number)
            break
        else:
            print('Please choose from only available options!')
            continue
    print(f'Estimated answer: {answer}')


if __name__ == '__main__':
    main()
