# ===========================Numbers========================
# Starting with any positive integer,
# replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers,
# while those that do not end in 1 are unhappy numbers.
# Display an example of your output here. Find first 8 happy numbers.

def extract_digits(number):
    digits = []
    while int(number) > 0:
        digits.append(int(number % 10))
        number = number / 10
    return digits[::-1]


def is_happy(num):
    previous_ones = []
    while True:
        answer = 0
        digits = extract_digits(num)
        for i in digits:
            answer += i**2
        if answer == 1:
            return True
        elif answer in previous_ones:
            return False
        else:
            num = answer
            previous_ones.append(num)


def main(num):
    happy_ones = []
    count = 0
    while count < 8:
        if is_happy(num):
            happy_ones.append(num)
            count += 1
        num += 1
    return happy_ones


if __name__ == '__main__':
    print(main(int(input())))
