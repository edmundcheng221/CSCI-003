"""
Homework #05
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-24

"""


def to_pig_latin(string):
    string = string.lower()
    vowel = 'aeiouAEIOU'
    for i in string:
        if string[:].isspace() or not string[:].isalpha():
            return string
            break
        elif len(string) == 1:
            return string
            break
        elif string[0] in vowel:
            string = string + 'way'
            break
        elif string[0:2] == 'sh' or string[0:2] == 'ch' or string[0:2] == 'th' or string[0:2] == 'qa':
            string = string[2:len(string)+1] + string[0:2]
            string = string + 'ay'
            break
        else:
            string = string[1:len(string)+1] + string[0]
            string = string + 'ay'
            break
    return string


assert to_pig_latin('hello world') == 'hello world', "string with space/non-letter characters should return the same"

assert to_pig_latin('s') == 's', "string of 1 letter should return the same"

assert to_pig_latin('chillax') == 'illaxchay', "for strings beginning with 'ch', 'sh', 'th', or 'qa', place the two letters at the end and add an 'ay' after that"

assert to_pig_latin('yolo') == 'oloyay', "for strings beginning with consonants, place the first letter at the end and add an 'ay' after that"


# Test


if __name__ == '__main__':
    print(to_pig_latin('u mad bro')) # u mad bro
    print(to_pig_latin('a')) # a
    print(to_pig_latin('thimble')) #imblethay
    print(to_pig_latin('narwhal')) #arwhalnay
    print(to_pig_latin('at'))  # atway