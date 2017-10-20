import math

def print_formatted(number):
    # your code goes here
    i = 0
    width = int(math.log(number, 2)) + 2
    first = width - 1
    while i < number:
        i += 1
        o = '{0:o}'.format(i)   #converting to Octal
        h = '{0:X}'.format(i)   #converting to Hex
        b = '{0:b}'.format(i)   #converting to Decimal
        print('{0:>{5}}{1:>{4}}{2:>{4}}{3:>{4}}'.format(i, o, h, b, width, first))

if __name__ == '__main__':
    n = int(input('Please Enter Number>>'))
    print_formatted(n)