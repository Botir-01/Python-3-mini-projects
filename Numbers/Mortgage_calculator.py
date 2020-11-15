# ===========================Numbers==========================
# Mortgage calculator
# Calculate the monthly payments of a fixed term mortgage
# over given Nth terms at a given interest rate.
# Figure out how long it will take the user to pay back the loan
# For added complexity, add an option for users to select the compounding interval
# Monthly, Weekly, Daily, Continually

class Mortgage:
    def __init__(self):
        while True:
            try:
                self.current_loan = float(input('Provide the amount of the loan: $'))
                if self.current_loan <= 50000:
                    print('Please provide loan higher than $50000')
                    continue
            except:
                print('Please provide correct numbers!')
                continue
            else:
                break
        while True:
            try:
                self.loan_term = float(input('The length of the loan (10/20/30) years: '))
                if self.loan_term == 10 or self.loan_term == 20 or self.loan_term == 30:
                    break
                else:
                    print('Please choose from provided options!')
                    continue
            except:
                print('Please provide correct values!')
                continue
        while True:
            try:
                self.annual_rate = float(input('Enter an annual interest rate: '))
            except:
                print('Please provide correct numbers!')
                continue
            else:
                break

    def monthly_payment(self):
        payment_length = self.loan_term * 12
        month_rate = self.annual_rate / 100 / 12
        return self.current_loan * month_rate * (1 + month_rate ** payment_length) / (
                1 + month_rate ** payment_length) - 1

    def __repr__(self):
        return f'Your loan amount: ${int(self.current_loan)} \n' \
               f'Annual interest rate: {self.annual_rate}% \n' \
               f'Loan term: {int(self.loan_term)} years \n' \
               f'Monthly payment: ${Mortgage.monthly_payment(self).__round__(3)}'


def main():
    mortgage_loan = Mortgage()
    print(mortgage_loan)


if __name__ == '__main__':
    main()
