"""
Homework #09
CSCI-UA 0003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-22
"""

import random
from os import system

thesaurus = {
    "happy":["glad",  "blissful", "ecstatic", "at ease"],
    "sad":["bleak", "blue", "depressed"]
}


def remove_punctuation(string):
    new_string = ""
    for i in string:
        if i.isalnum() or i == " ":
            new_string += i
    return new_string.lower()


phrase = input("Enter a phrase:\n> ")
new_phrase = remove_punctuation(phrase).split(" ")
newest = ""
for word in new_phrase:
    k = word.lower()
    if k in thesaurus:
        value = random.randint(0, len(thesaurus[k]) - 1)
        newest += thesaurus[k][value].upper() + " "
    else:
        newest += word + " "
print(newest)

# part 2
thesaurus_dict = {}
f = open('thesaurus.txt', 'r')
for line in f:
    new_list = line.strip().split(",")
    thesaurus_dict[new_list[0]] = new_list[1:]

phrase = input("Enter a phrase:\n> ")
new_phrase = remove_punctuation(phrase).split(" ")
newest = ""
for word in new_phrase:
    k = word.lower()
    if k == 'the':
        newest += k + ' '
    elif k == 'we':
        newest += k + ' '
    elif k not in thesaurus_dict:
        newest += k + ' '
    elif k in thesaurus_dict:
        value = random.randint(0, len(thesaurus_dict[k]) - 1)
        newest += thesaurus_dict[k][value].upper() + " "


print(newest)
f.close()

# part 3

def remove_punctuation2(string):
    new_string = ""
    for i in string:
        if i == '\n':
            new_string += ' '
        elif i.isalnum() or i == " ":
            new_string += i
    return new_string.lower()


bb = open('bad_blood.txt', 'r').read()
new = remove_punctuation2(bb)

print(new)

thesaurus_dict = {}
f = open('thesaurus.txt', 'r')
for line in f:
    new_list = line.strip().split(",")
    thesaurus_dict[new_list[0]] = new_list[1:]

phrase = new
new_phrase = remove_punctuation(phrase).split(" ")
newest = ""
count = 1
for word in new_phrase:
    count += 1
    k = word.lower()
    if k == 'the':
        newest += k + ' '
    elif k == 'we':
        newest += k + ' '
    elif k not in thesaurus_dict:
        newest += k + ' '
    elif count % 2 == 0:  # this is a valid approach in substituting 50% of the words!
        newest += k + ' '
    elif k in thesaurus_dict and count % 2 == 1:
        value = random.randint(0, len(thesaurus_dict[k]) - 1)
        newest += thesaurus_dict[k][value].upper() + " "
print(newest)
# print('PROFIT')
f.close()
# optional part


if __name__ == '__main__':
    system("say -i -v Fiona " + "\"" + newest + "\"")
# this part would have the computer sing the lyrics for you
#
# system("say -i -v Fiona " + "\"" + newest + "\"")