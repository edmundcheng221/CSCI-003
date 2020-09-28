"""
Homework #02
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-09-27

PWEASE GRADE EZ, I TRIED MY BEST
"""
from random import *
num_words = randint(3,6)  # how many words we ask for
print(f'I\'ll need {num_words} words:')

shortest = ''
for i in range(num_words):
    words1 = input(f'Word #{i+1} please!\n> ')
    if len(shortest) == 0:
        shortest = words1         # Replace empty string with first word so we don't get an empty string as answer
        i += 1
    elif len(shortest) < len(words1):       # increment thru words to find smallest
        i += 1
    else:
        shortest = words1
        i += 1


list_of_words = ''
# increment thru words to find largest. Don't need to worry about getting empty string because we are looking for largest
for i in range(num_words):
    words2 = input(f'Word #{i+1} please!\n> ')
    if len(list_of_words) <= len(words2):
        list_of_words = words2
        i += 1
    else:
        i += 1

print(f'Shortest: {shortest}')
print(f'Longest: {list_of_words}')

summation = 0
original_num_words = num_words
while num_words != 0:    # increment until there are no more words
    for i in range(num_words):
        # increment thru words summing the lengths to a variable to get total
        words3 = input(f'Word #{i + 1} please!\n> ')
        summation += len(words3)
        num_words -= 1     # subtract 1 from num_words after each loop
print(summation)
average = summation/original_num_words
print(average)