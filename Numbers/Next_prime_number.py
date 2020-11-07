# ===========================Numbers==========================
# Have the program to find prime numbers until the user chooses to stop asking for the next one

def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** 0.5 + 1), 2):
            if num % i == 0:
                return False
    return True


def prime_gen(prime):
    next_prime = prime + 1
    while True:
        if not is_prime(next_prime):
            next_prime += 1
        else:
            break
    return next_prime


def main():
    current_prime = 2
    while True:
        user_input = input('Would you like to see the next prime number (y/n): ')
        if user_input.lower()[0] == 'y':
            print(current_prime)
            current_prime = prime_gen(current_prime)
        elif user_input.lower().startswith('n'):
            print('Thanks!')
            break
        else:
            continue


if __name__ == '__main__':
    main()
