
def binarydecimal_conv():
    try:
        menu = int(input("choose an option: \n 1. Decimal to binary \n 2. Binary to decimal"))

        if menu == 1:
            decimal = int(input('input your decimal number'))
            print(f'Binar: {bin(decimal)}')
        elif menu == 2:
            binary = input('enter a binary number')
            print(f'Decimal : {int(binary, 2)}')
    except ValueError:
        print('please input a valid option')
binarydecimal_conv()
