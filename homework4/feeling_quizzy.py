"""
Homework #04
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-14

"""
import funcynum
import random

# print(funcynum.print_two('*', 5))

num_prob = int(input('How many problems?\n> '))
while num_prob not in range(3, 21):
    print('Please enter a number between 3 and 20...')
    num_prob = int(input('How many problems?\n> '))

char = input('What character do you want the numbers to be made of?\n> ')

while len(char) > 1:
    print('Please enter a single character!')
    char = input('What character do you want the numbers to be made of?\n> ')

width = int(input('How wide do you want each number to be?\n> '))
if width > 3:
    print('Oops… defaulting to width 3')
    width = 3

count_correct = 0
count_tot = 0


while num_prob > 0:
    random_number1 = random.randint(0,9)
    random_number2 = random.randint(0,9)
    operation = random.randint(1,2)
    if operation == 1:
        operation = '+'
    else:
        operation = '-'
    print('What is...')

    if random_number1 == 0:
        print(funcynum.print_zero(char, width) + '\n')
    elif random_number1 == 1:
        print(funcynum.print_one(char, width) + '\n')
    elif random_number1 == 2:
        print(funcynum.print_two(char, width) + '\n')
    elif random_number1 == 3:
        print(funcynum.print_three(char, width) + '\n')
    elif random_number1 == 4:
        print(funcynum.print_four(char, width) + '\n')
    elif random_number1 == 5:
        print(funcynum.print_five(char, width) + '\n')
    elif random_number1 == 6:
        print(funcynum.print_six(char, width) + '\n')
    elif random_number1 == 7:
        print(funcynum.print_seven(char, width) + '\n')
    elif random_number1 == 8:
        print(funcynum.print_eight(char, width) + '\n')
    elif random_number1 == 9:
        print(funcynum.print_nine(char, width) + '\n')

    if operation == '+':
        print(funcynum.print_plus(char, width) + '\n')
    else:
        print(funcynum.print_minus(char, width) + '\n')

    if random_number2 == 0:
        print(funcynum.print_zero(char, width) + '\n')
    elif random_number2 == 1:
        print(funcynum.print_one(char, width) + '\n')
    elif random_number2 == 2:
        print(funcynum.print_two(char, width) + '\n')
    elif random_number2 == 3:
        print(funcynum.print_three(char, width) + '\n')
    elif random_number2 == 4:
        print(funcynum.print_four(char, width) + '\n')
    elif random_number2 == 5:
        print(funcynum.print_five(char, width) + '\n')
    elif random_number2 == 6:
        print(funcynum.print_six(char, width) + '\n')
    elif random_number2 == 7:
        print(funcynum.print_seven(char, width) + '\n')
    elif random_number2 == 8:
        print(funcynum.print_eight(char, width) + '\n')
    elif random_number2 == 9:
        print(funcynum.print_nine(char, width) + '\n')

    answer = int(input('=')) # what is the user's answer?

    if operation == '+':
        correct_answer = random_number1 + random_number2
    else:
        correct_answer = random_number1 - random_number2

    correct = funcynum.check_answer(random_number1,random_number2,answer, operation)
    # count_correct = 0
    # count_tot = 0
    # while num_prob > 0:
    if correct == True:
        print('Correct!')
        count_correct += 1
        count_tot += 1
        num_prob -= 1

    else:
        print(f'Nope the answer is {correct_answer}')
        count_tot += 1
        num_prob -= 1

percentage = (count_correct / count_tot)* 100
new_percentage = format(percentage, '.2f')
print(f'You got {new_percentage}% correct ({count_correct} out of {count_tot})')
