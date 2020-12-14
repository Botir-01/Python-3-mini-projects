# ============================Numbers============================
# Unit Converter (temp, currency, volume, mass, and more)
# Converts various units between one another. The user enters the type of unit being entered.
# The type of unit they want to convert to and then the value.
# The program will then make conversion.
import urllib.request
import json


def celsius_to_fahrenheit(num):
    return (num * 9 / 5) + 32


def fahrenheit_to_celsius(num):
    return (num - 32) * 5 / 9


def currency_exchange(con_from, con_to, value):
    curr_page = urllib.request.urlopen(
        'http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62')
    obj = curr_page.read().decode(encoding='UTF-8')
    content = json.loads(obj)
    try:
        from_to = content['rates'][con_from]
        to = content['rates'][con_to]
        amount = to / from_to
        result = amount * value
    except:
        raise NameError
    return result


def liter_to_milliliter(num):
    return num * 1000


def milliliter_to_liter(num):
    return num / 1000


def kilograms_to_grams(num):
    return num * 1000


def grams_to_kilograms(num):
    return num / 1000


def kilograms_to_pounds(num):
    return num * 2.205


def pounds_to_kilograms(num):
    return num / 2.205


def main():
    value = 0
    con_from = 0
    con_to = 0
    while True:
        try:
            options = int(input('Please, choose of these options: \n'
                                '1 for Celsius to Fahrenheit \n'
                                '2 for Fahrenheit to Celsius \n'
                                '3 for Currency Converter \n'
                                '4 for Liter to Milliliter \n'
                                '5 for Milliliter to Liter \n'
                                '6 for Kilograms to Grams \n'
                                '7 for Grams to Kilograms \n'
                                '8 for Kilograms to Pounds \n'
                                '9 for Pounds to Kilograms: '))
            if options == 1:
                while True:
                    try:
                        value = float(input('Please, enter some value to convert: '))
                    except:
                        print('Provide correct inputs')
                        continue
                    else:
                        break
                answer = celsius_to_fahrenheit(value)
                print(f'It is {answer}°F')
            elif options == 2:
                while True:
                    try:
                        value = float(input('Please, enter some value to convert: '))
                    except:
                        print('Provide correct inputs')
                        continue
                    else:
                        break
                answer = fahrenheit_to_celsius(value)
                print(f'It is {answer}°C')
            elif options == 3:
                while True:
                    try:
                        con_from = input('The currency to convert from: ')
                        con_to = input('The currency to convert to: ')
                        value = float(input('Enter some value that should be converted: '))
                    except:
                        print('Please provide correct inputs!')
                        continue
                    else:
                        break
                result = currency_exchange(con_from, con_to, value)
                print(f'It is {result}')
            elif options == 4:
                while True:
                    try:
                        value = float(input('Please, enter some value to convert: '))
                    except:
                        print('Provide correct inputs')
                        continue
                    else:
                        break
                answer = liter_to_milliliter(value)
                print(f'It is {answer}mL')
            elif options == 5:
                while True:
                    try:
                        value = float(input('Please, enter some value to convert: '))
                    except:
                        print('Provide correct inputs')
                        continue
                    else:
                        break
                answer = milliliter_to_liter(value)
                print(f'It is {answer}L')
            elif options == 6:
                while True:
                    try:
                        value = float(input('Please, enter some value to convert: '))
                    except:
                        print('Provide correct inputs')
                        continue
                    else:
                        break
                answer = kilograms_to_grams(value)
                print(f'It is {answer}g')
            elif options == 7:
                while True:
                    try:
                        value = float(input('Please, enter some value to convert: '))
                    except:
                        print('Provide correct inputs')
                        continue
                    else:
                        break
                answer = grams_to_kilograms(value)
                print(f'It is {answer}kg')
            elif options == 8:
                while True:
                    try:
                        value = float(input('Please, enter some value to convert: '))
                    except:
                        print('Provide correct inputs')
                        continue
                    else:
                        break
                answer = kilograms_to_pounds(value)
                print(f'It is {answer}Ibs')
            elif options == 9:
                while True:
                    try:
                        value = float(input('Please, enter some value to convert: '))
                    except:
                        print('Provide correct inputs')
                        continue
                    else:
                        break
                answer = pounds_to_kilograms(value)
                print(f'It is {answer}kg')
        except:
            print('Please choose from types provided!')
            continue
        else:
            break


if __name__ == '__main__':
    main()
