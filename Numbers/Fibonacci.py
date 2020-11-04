# ===============================Numbers=======================
# Enter a number
# Have the program to generate the Fibonacci sequence to that number or to the Nth number

def fibonacci(num):
    result = []
    for n in range(0, num):
        if n == 0:
            result.append(n)
        elif n == 1:
            result.append(n)
        else:
            result.append(result[n - 1] + result[n - 2])

    for i in range(len(result)):
        result[i] = str(result[i])
    return ", ".join(result)


def main():
    num = 0
    while True:
        try:
            num = int(input('Enter a number to generate Fibonacci sequence to that number: '))
        except:
            print('You did not enter an integer!')
            continue
        else:
            break
    print(fibonacci(num))


if __name__ == '__main__':
    main()
