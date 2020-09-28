"""
Homework #02
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-09-27

PWEASE GRADE EZ, I TRIED MY BEST
"""
welcome = f'/// WELCOME \\\\'+'\\'
statement = 'Perhaps I can help you calculate $$$ for yr tip!'
print(format('~'*len(welcome), '>'+str((len(statement)+12)//2)))
print(format(welcome, '>'+str((len(statement)+12)//2)))

print(format('~'*len(welcome), '>'+str((len(statement)+12)//2)))
print(statement)

num_people = int(input('How many people?\n> '))
cost = float(input('How much did it cost?\n> '))
if num_people < 6:
    service = input('How was the service (terrible, poor, ok, good, great)\n> ')
    if service == 'terrible':
        percentage = 0
    elif service == 'poor':
        tip = cost * 0.10
    elif service == 'ok':
        tip = cost * 0.15
    elif service == 'good':
        tip = cost * 0.20
    elif service == 'great':
        tip = cost * 0.25
    else:
        tip = cost * 0.20
        print('The default tip value will be used')

elif num_people >= 6:
    tip = cost * 0.20
rounded_tip = format(tip, '.2f');

print(f'You should probably tip ${rounded_tip}!')