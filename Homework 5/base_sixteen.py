"""
Homework #05
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-24

"""


def convert(val):
    symbol = val[0:2]
    if symbol != '0x':    # must start with 0x
        return None
    hex = val[2:]
    hex_digits = set('0123456789ABCDEFabcdef')
    for character in hex:
        if character not in hex_digits: # characters must be in the set
            return None
    dictionary = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    power = 0
    result = 0
    for i in range(len(hex)-1,-1,-1):
        if hex[i].isalpha():
            result += dictionary[hex[i]] * (16**power)
        else:
            result += int(hex[i]) * (16**power)
        power += 1
    return result


if __name__ == '__main__':
    print(convert('0x0001'))
    print(convert('0x0010'))
    print(convert('0x21'))
    print(convert('0xAE'))
    print(convert('0x7BF5'))
    print(convert('0x7bf5'))
    print(convert('2AF3'))
    print(convert('0xZZZ'))


assert convert('0x1AC') == 428, "given example muist convert to 428"

assert type(convert('0x7bf5')) == int , "must convert to an integer"