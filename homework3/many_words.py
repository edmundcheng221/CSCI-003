"""
Homework #03
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-02

PWEASE GRADE EZ, I TRIED MY BEST
"""


def rev_string():
    question = int(input('How many words?\n> '))
    string = ''
    for i in range(question):
        word = input('Word please!\n> ')
        string += " "+word
    words = string.split(' ')   # split up the string

    reverse_string = ' '.join(reversed(words)) # reverse the split string and join

    return reverse_string # return the reversed string

print(rev_string())


