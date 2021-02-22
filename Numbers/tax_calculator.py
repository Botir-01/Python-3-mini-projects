# =================================Numbers============================
# Asks the user to enter a cost and either a country or state tax.
# It then returns the tax plus the total cost with tax.


def total_calc(cost):
    country_tax = 0
    while True:
        try:
            country_tax = float(input("Enter state's tax: "))
        except:
            print("Please enter some value!")
            continue
        else:
            break
    return (cost + cost * (country_tax / 100)), country_tax


def main():
    cost = 0
    while True:
        try:
            cost = float(input("Enter the cost: "))
        except:
            print("Please provide certain values!")
            continue
        else:
            break
    total_cost, tax = total_calc(cost)
    print(f'================================\n'
          f'The country/state tax: {tax}% \n'
          f'The cost: ${round(cost)} \n'
          f'The total cost: ${round(total_cost)}')


if __name__ == '__main__':
    main()
