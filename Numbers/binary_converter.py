# =============================Numbers=================================
# Develop a converter to convert a decimal number to binary
# or a binary number to its decimal equivalent


def decimal_to_binary(num):
    """ Takes a decimal number as an argument, converts to binary and returns it
    negative, null, positive numbers are handled
    """
    binary_list = []
    if num == 0:
        return num
    elif int(num) > 0:
        while int(num) > 0:
            binary_list.append(int(num) % 2)
            num /= 2
        for i in range(len(binary_list)):
            binary_list[i] = str(binary_list[i])
        return ''.join(reversed(binary_list))
    else:
        while int(abs(num)) > 0:
            binary_list.append(int(abs(num) % 2))
            num = abs(num) / 2
        for i in range(len(binary_list)):
            binary_list[i] = str(binary_list[i])
        return '-' + ''.join(reversed(binary_list))


def binary_to_decimal(num):
    """ Takes a binary number and converts it to a decimal one
    negative, null, positive are handled.
    """
    result = 0
    if num >= 0:
        string_b_numbers = str(num)
        for power, number in reversed(list(enumerate(reversed(string_b_numbers)))):
            result += int(number) * 2 ** power
        return result
    else:
        string_b_numbers = str(abs(num))
        for power, number in reversed(list(enumerate(reversed(string_b_numbers)))):
            result += int(number) * 2 ** power
        return '-' + str(result)


def main():
    binary_number = 0
    decimal_number = 0
    while True:
        choice = input('Type d for a decimal converter or b for binary one: ')
        if choice.lower()[0] == 'b':
            while True:
                try:
                    binary_number = int(input('Enter a binary number to convert to decimal: '))
                except:
                    print('You did not enter a binary number')
                    continue
                else:
                    break
            print(binary_to_decimal(binary_number))
            break
        elif choice.lower()[0] == 'd':
            while True:
                try:
                    decimal_number = int(input('Enter a decimal number to convert to binary: '))
                except:
                    print('You did not enter a decimal number')
                    continue
                else:
                    break
            print(decimal_to_binary(decimal_number))
            break
        else:
            print('Please choose one of the options')
            continue


if __name__ == '__main__':
    main()
