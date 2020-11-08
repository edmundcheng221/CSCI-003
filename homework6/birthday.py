"""
Homework #06
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-01

"""
import mydate
import listutils

num_times = int(input('How many times should I run the simulation?\n> '))
num_birthdays = int(input('How many birthdays should I generate per trial?\n> '))


def simulations(num_birth):
    birthday = []
    while num_birth > 0:
        birthday.append(list(mydate.generate_date(2014, 2017)))
        num_birth -= 1
    result = mydate.remove_years(birthday)
    return result


num_repeat = 0
count = 0
while num_times > 0:
    lst = simulations(num_birthdays)
    new = listutils.stringify_elements(lst)
    set_list = set(new)
    num_duplicates = len(lst) - len(set_list)
    element_unique = list(set_list)

    duplicates = []
    for x in lst:
        if lst.count(x) > 1:
            duplicates += [x]
    months = '('

    for things in range(len(duplicates)):
        if len(duplicates)>0:
            # duplicates[things][0] = (duplicates[0])
            months += mydate.month_num_to_string(duplicates[things][0])
            months += ' '
            months += str(duplicates[things][1])
            months += ','
            months += ' '

    months += ')'


    if num_duplicates > 0:
        print(f'Trial #{count + 1}: {num_duplicates} dates occurs more than once!' + months)
        num_repeat += 1
    else:
        print(f'Trial #{count}: No dates are the same!')

    num_times -= 1
    count += 1

print('Results:')
print('======')
print(f'Out of {count} trials, {num_repeat} had dates that were repeated')
chance = format((num_repeat*100/count), '.2f')
print(chance)
print(f'We can conclude that you have a {chance}% of of sharing a birthday with someone if you are in a group of '
      f'{num_birthdays} people')