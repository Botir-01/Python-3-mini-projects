# =====================================Numbers==================================
# Enter a number
# find all prime factors (if there are any) and display them.


def prime_factorization(num):
    prime_factors = []
    while num % 2 == 0:
        num = num / 2
        prime_factors.append(2)
    for n in range(3, int(num) ** 2, 2):
        while num % n == 0:
            num = num / n
            prime_factors.append(int(n))
    if num > 2:
        prime_factors.append(num)
    for i in range(len(prime_factors)):
        prime_factors[i] = str(prime_factors[i])
    return ', '.join(prime_factors)


def main():
    user_input = 0
    while True:
        try:
            user_input = int(input('Enter a number to find its prime factors: '))
        except:
            print('You did not enter an integer!')
            continue
        else:
            break
    if user_input == 0 or user_input == 1:
        return print("The number doesn't have its prime numbers!")
    print(prime_factorization(user_input))


if __name__ == '__main__':
    main()
