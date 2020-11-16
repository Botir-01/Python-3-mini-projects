# ====================================Numbers=================================
# The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
def change(cost, money):
    changes = money - cost
    dollars = int(changes)
    coins = ((changes - dollars).__round__(1) * 100)
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while dollars >= 20:
        twenties = dollars / 20
        dollars = dollars % 20
    while dollars >= 10:
        tens = dollars / 10
        dollars = dollars % 10
    while dollars >= 5:
        fives = dollars / 5
        dollars = dollars % 5
    while dollars >= 1:
        ones = dollars / 1
        dollars = dollars % 1
    while coins >= 25:
        quarters = coins / 25
        coins = coins % 25
    while coins >= 10:
        dimes = coins / 10
        coins = coins % 10
    while coins >= 5:
        nickels = coins / 5
        coins = coins % 5
    while coins >= 1:
        pennies = coins / 1
        coins = coins % 1
    print(f'Your change: ${changes:.2f} \n'
          f'Twenties: {int(twenties)} \n'
          f'Tens: {int(tens)} \n'
          f'Fives: {int(fives)} \n'
          f'Ones: {int(ones)} \n'
          f'Quarters: {int(quarters)} \n'
          f'Dimes: {int(dimes)} \n'
          f'Nickels: {int(nickels)} \n'
          f'Pennies: {int(pennies)}')


def main():
    product_cost = 0
    money_given = 0
    while True:
        try:
            product_cost = float(input('Enter the cost of the product: $'))
            if product_cost <= 0:
                print('Enter correct values!')
                continue
        except:
            print('Provide numbers!')
            continue
        else:
            break
    while True:
        try:
            money_given = float(input('How much money you gave?: $'))
            if money_given <= 0:
                print('Please provide correct values!')
                continue
        except:
            print('Please enter correct numbers!')
            continue
        else:
            break
    change(product_cost, money_given)


if __name__ == '__main__':
    main()
