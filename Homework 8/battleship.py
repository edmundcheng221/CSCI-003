"""
Homework #08
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-15
"""
import random


def load_from_file(name_of_file:str):
    nested = []
    str_to_list = name_of_file.split('\n')
    for ele in str_to_list:
        stringed = ele.split('\n')
        nested += stringed
    # print(nested)
    board = [char.split(', ') for char in nested]
    # print(ans)
    for thing in board:
        print(thing)

    return board


def save_to_file(name_of_file:str, board):
    with open(name_of_file, 'w') as save:
        save.write(str(board))


def main():
    load = input('Would you like to load a file?\n> ')
    if load == 'yes' or load == 'YES':
        file_name = input('What\'s the name of the file you\'d like to load?\n> ')
        try:
            with open(file_name, 'r') as file:
                load_from_file(file_name)
        except FileNotFoundError:
            lst = [['0 0 0 0 0'], ['0 0 0 0 0'], ['0 0 0 0 0'], ['0 0 0 0 0'], ['0 0 0 0 0']]
            # print(lst)
    else:
        lst = [['0 0 0 0 0'], ['0 0 0 0 0'], ['0 0 0 0 0'], ['0 0 0 0 0'], ['0 0 0 0 0']]
        # print(lst)

set_location = input('Do you want to set the location of the computer\'s ship?\nType row,col to set or press ENTER/RETURN to skip\n> ')

if set_location == '':
    row = random.randint(1,5) # rows 1 to 5
    # print(type(row))
    col = random.randint(1,5) # rows 1 to 5
    location = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', '_', 'o', 'o', 'o'], ['o', 'o', '_', 'o', 'o']]

else: # type 1,2 for example, no paranthesis/spaces/etc
    location = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', '_', 'o', 'o', 'o'], ['o', 'o', '_', 'o', 'o']]
    row = int(set_location[0]) - 1
    col = int(set_location[-1]) - 1

outlst = [' '.join(str(c) for c in lst) for lst in location]
print(outlst)
list_emp = []
for array in outlst:
    for let in array:
        list_emp.append(let)
for n,loop in enumerate(list_emp):
    if loop == '_':
        list_emp[n] = ' '

new_list = [list_emp[:9:2]]+[list_emp[9:18:2]]+[list_emp[18:27:2]]+[list_emp[27:36:2]]+[list_emp[36:45:2]]
print(new_list)


string_var = ''
outlst2 = [' '.join(str(c) for c in lst) for lst in new_list]
for var in outlst2:
    string_var += var
    string_var += '\n'
# print(outlst)
print(string_var)

 # part 4
i = 0
while i < 1:
    user_question = input('(s)ave, (q)uit or enter a row and column\n> ')
    if int(user_question[0]) < 5 or int(user_question[2]) < 5 or int(user_question[1]) == ',':
        i += 1
    elif user_question == 'q':
        i += 1
    elif user_question == 's':
        file_input = input('Enter the name of the file\n> ')
        load = load_from_file(file_input)
        save_to_file('save.txt', load)
        i += 1
    elif user_question != 'q' or user_question != 's' or len(user_question) != 3 or int(user_question[0]) >= 5 or int(user_question[2]) >= 5:
        print(new_list)


starter = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]


def replace_charX(user_question): # function to replace user input index with the letter 'X'
    outlst = [' '.join(str(c) for c in lst) for lst in starter]
    print(outlst)
    list_emp = []
    for array in outlst:
        for let in array:
            list_emp.append(let)
    # print(list_emp)
    # for n, loop in enumerate(list_emp):
    #     if loop == 'o':
    #         list_emp[n] = 'X'

    new_list = [list_emp[:9:2]] + [list_emp[9:18:2]] + [list_emp[18:27:2]] + [list_emp[27:36:2]] + [list_emp[36:45:2]]
    new_list[int(user_question[0])][int(user_question[2])] = 'X'
    print(new_list)

    string_var = ''
    outlst2 = [' '.join(str(c) for c in lst) for lst in new_list]
    for var in outlst2:
        string_var += var
        string_var += '\n'
    # print(outlst)
    print(string_var)
replace_charX('1,2')


def replace_char_space(user_question): # function to replace the user input index with a space
    outlst = [' '.join(str(c) for c in lst) for lst in starter]
    print(outlst)
    list_emp = []
    for array in outlst:
        for let in array:
            list_emp.append(let)
    new_list = [list_emp[:9:2]] + [list_emp[9:18:2]] + [list_emp[18:27:2]] + [list_emp[27:36:2]] + [list_emp[36:45:2]]
    new_list[int(user_question[0])][int(user_question[2])] = ' '
    print(new_list)

    string_var = ''
    outlst2 = [' '.join(str(c) for c in lst) for lst in new_list]
    for var in outlst2:
        string_var += var
        string_var += '\n'
    # print(outlst)
    print(string_var)
win = 0
# Note: Counting starts at 0. So if you want row 1 col 2, you have to put 0,1 for in user question
while win < 1:
    if user_question == str(row) + ',' + str(col):
        print('You win the game!')
        print(f'The boat was at row {row} and column {col}')
        current_board = [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]
        replace_charX(user_question)
        win += 1
        break
    elif user_question == 'q':
        win += 1
        break
    elif user_question == 's':
        file_in = input('Enter the name of the file\n> ')
        loads = load_from_file(file_in)
        save_to_file('save.txt', loads)
        win += 1
        break
    else:
        replace_char_space(user_question)
        # starter = replace_char_space(user_question)
        user_question = input('(s)ave, (q)uit or enter a row and column\n> ')





if __name__ == '__main__':
    # string_data = 'o o o o o\no o X o o\no o o o o\no _ o o o\no o _ o o'
    # # print(string_data)
    # res = load_from_file(string_data)
    # # print(res)
    # save_to_file('save.txt', res)
    main()



