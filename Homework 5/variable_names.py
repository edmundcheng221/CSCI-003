"""
Homework #05
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-24

"""


def is_valid_name(name):
    mapping = '0123456789'
    special = '!#@$%^&*()[]{}|~:;+=<>?/' # i think those are all the special characters....
    if len(name) == 0: # returns false becuase the string is empty
        return False
    elif name[0] in mapping: # cannot start with a numeric
        return False
    for letter in name:
        if letter in special: # if any of the letters are the special characters
            return False

    return True # if passes all of the following cases, then it is a valid name


if __name__ == '__main__':
    trial = 0
    while trial < 3:
        name = input('Variable name plz\n> ')
        if is_valid_name(name):
            print('True')
            break
        else:
            print('False')
            trial += 1


assert is_valid_name('1asdf') == False, "Cannot start variable with number"
assert is_valid_name('#foo')  == False, "Cannot start variable with a special character"
assert is_valid_name('asdf1') == True, "Obeys all rules"
assert is_valid_name('_foo') == True, "Obeys all rules"
assert is_valid_name('f_oo') == True, "Obeys all rules"