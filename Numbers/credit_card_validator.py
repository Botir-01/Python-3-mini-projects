# =========================Numbers==============================
# Takes in a credit card number that is 16 digit long and validates
# it to make sure that is a valid number (look into how credit
# cards use a checksum).

def credit_card_checker(credit_number):
    def_length = 16
    double = 2
    number_to_check = ''
    result = 0
    for i in credit_number:
        if i != ' ':
            number_to_check += i
    if def_length == len(number_to_check):
        last_number = number_to_check[-1]  # grabs the last number of the credit card number
        number_to_check = number_to_check[0:def_length - 1]  # grabs remaining part
        for num in range(0, len(number_to_check), 1):
            if num % 2 == 0 or num == 0:  # for multiplication by 2
                number = int(number_to_check[num]) * double
                if number > 9:  # checks for two-digit number
                    number -= 9
                result += number
            else:
                result += int(number_to_check[num])
        result += int(last_number)
        if result % 10 == 0:
            print('The credit card number is valid!')
        else:
            print('Invalid credit card number, make sure to provide correct numbers!')

    else:
        print('Ops, values are incorrect! \n'
              'Please try again!')


def main():
    user_card = input('Please provide a credit number to validate: ')
    credit_card_checker(user_card)


if __name__ == '__main__':
    main()
