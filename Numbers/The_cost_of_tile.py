# ============================Numbers==================
# find the cost of tile to cover w and h of floor
# calculate the total cost of tile it would take to cover
# a floor plan of width and height, using a cost entered by the user


def exception_handle(item):
    while True:
        try:
            item = float(input(f'Please enter the {item}: '))
        except:
            print('Please provide appropriate numbers!')
            continue
        else:
            break
    return item


def main():
    width = exception_handle('width')
    height = exception_handle('height')
    cost = exception_handle('cost')
    print(f'Your cost for the {int(width)}x{int(height)} floor is {width * height * cost}$')


if __name__ == "__main__":
    main()
