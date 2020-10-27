"""
Homework #05
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-24

"""

# Part 1


def num_to_let(num):
    length = len(num)
    index = ''
    substring = ''
    for i in range(length):
        if (num[i].isnumeric()):
            substring += num[i]
            if (num[i].isnumeric() and i == length - 1):
                index += chr(int(substring) + 64)

        else:
            if (not substring):
                pass
            else:
                number = int(substring) + 64
                if (number < 65 or number > 90):
                    pass
                else:
                    index += chr(number)
                substring = ''
    print(index)


if __name__ == '__main__':
    num_to_let('1-13-26')
    num_to_let('1-100-26')
    num_to_let('1-!-?')
    num_to_let('---26')

assert num_to_let('1-!-?') == 'A', "given expected result"
# PART 2


def let_to_num(letters):
    string = '' #create empty string to add values in later
    controller = False # initialize as false
    for i in letters: # loops thru word
        if i.isalpha(): # checks of alphabet
            string += str(ord(i.upper())-64)+"-"
            controller = True # change the controller to true
    if controller: #if true
        return string[:-1] # if true return the encoded number
    return string # returns empty string if false


if __name__ == '__main__':
    print(let_to_num('AZ'))
    print(let_to_num(''))
    print(let_to_num('A?Z'))
    print(let_to_num('AZ?'))
    print(let_to_num('AbzC'))

assert num_to_let('AbzC') == '1-2-26-3', "given expected result"

# Part 3


def conversion():
    while True:
        choice = input('(n)um_to_let, (l)et_to_num or (q)uit?\n> ').lower()
        if choice == 'n':
            string = input('What string do you want to use your function on?\n> ')
            print(num_to_let(string))
        elif choice == 'l':
            string = input('What string do you want to use your function on?\n> ')
            print(let_to_num(string))
        elif choice == 'q':
            break


if __name__ == '__main__':
    conversion()

