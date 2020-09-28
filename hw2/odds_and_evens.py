"""
Homework #02
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-09-27

PWEASE GRADE EZ, I TRIED MY BEST
"""
import random
print('Let\'s play odds and evens')
odd_or_even = input('Do you want to be (odds) or (evens)?\n> ')
stopper = 0
while stopper < 1:   # while loop controller
    if odd_or_even == 'odds':
        print('you are odds')
        human = odd_or_even    # human is odd/even depending on which they choose
        machine = 'evens'           # if human is odd, machine is even
        stopper += 1
    elif odd_or_even == 'evens':
        print('you are evens')
        human = odd_or_even           # if human is even, machine is odd
        machine = 'odds'
        stopper += 1
    else:
        odd_or_even = input('Do you want to be (odds) or (evens)?\n> ')   # if user does not select valid input, we ask again
num_wins = int(input('What do you want to play up to?\n> '))
print(f'Okay, {num_wins} wins will win the entire game!')
if num_wins < 1:
    print('NO ONE WINS. GAME OVER!')
elif num_wins > 0:
    # if the number of wins is greater than 0, we proceed with the game
    # so far no one won so scores for both player and computer are 0
    player = 0
    computer = 0
    round_num = 1
    print(f'Round {round_num}') # print the current round of game
    print('=' * 5)
    print(f'player: {player}, computer: {computer}')
    num_fingers = int(input('How many fingers do you want to play?\n> '))

    while player < num_wins and computer < num_wins:  # whichever player gets the specified number of wins, wins
        print(f'Round {round_num}')
        print('=' * 5)
        print(f'number of wins')
        print(f'player: {player}, computer: {computer}')
        print(f'OK, player with {num_wins} wins first will win the game')
        if num_fingers == 1:    # player's choice
            print(f'Player played ☝️ finger (1)')
            num_comp = random.randint(1,2)
            if num_comp == 1:  #computer's choice
                print(f'Computer played ☝️ finger (1)')
                total = num_fingers + num_comp
                if total % 2 == 0 and human == 'evens':
                    print(f'Player scores 1 win')
                    player += 1
                    round_num += 1
                elif total % 2 == 0 and human != 'evens':
                    print(f'Computer scores 1 win')
                    computer += 1
                    round_num += 1
                elif total % 2 != 0 and machine == 'odds':
                    print(f'Computer scores 1 win')
                    computer += 1
                    round_num += 1
                else:
                    print('Player scores 1 win')
                    player += 1
                    round_num += 1
            elif num_comp == 2:   # computer's choice
                print(f'Player played ✌️️ fingers (2)')
                total = num_fingers + num_comp
                if total % 2 == 0 and human == 'evens':
                    print(f'Player scores 1 win')
                    player += 1
                    round_num += 1
                elif total % 2 == 0 and human != 'evens':
                    print(f'Computer scores 1 win')
                    computer += 1
                    round_num += 1
                elif total % 2 != 0 and machine == 'odds':
                    print(f'Computer scores 1 win')
                    computer += 1
                    round_num += 1
                else:
                    print('Player scores 1 win')
                    player += 1
                    round_num += 1

        elif num_fingers == 2: # player's choice
            print(f'Player played ✌️️ fingers (2)')
            num_comp = random.randint(1, 2)
            if num_comp == 1: # computer's choice
                print(f'Computer played ☝️ finger (1)')
                total = num_fingers + num_comp
                if total % 2 == 0 and human == 'evens':
                    print(f'Player scores 1 win')
                    player += 1
                    round_num += 1
                elif total % 2 == 0 and human != 'evens':
                    print(f'Computer scores 1 win')
                    computer += 1
                    round_num += 1
                elif total % 2 != 0 and machine == 'odds':
                    print(f'Computer scores 1 win')
                    computer += 1
                    round_num += 1
                else:
                    print('Player scores 1 win')
                    player += 1
                    round_num += 1
            elif num_comp == 2: # computer's choice
                print(f'Player played ✌️️ fingers (2)')
                total = num_fingers + num_comp
                if total % 2 == 0 and human == 'evens':
                    print(f'Player scores 1 win')
                    player += 1
                    round_num += 1
                elif total % 2 == 0 and human != 'evens':
                    print(f'Computer scores 1 win')
                    computer += 1
                    round_num += 1
                elif total % 2 != 0 and machine == 'odds':
                    print(f'Computer scores 1 win')
                    computer += 1
                    round_num += 1
                else:
                    print('Player scores 1 win')
                    player += 1
                    round_num += 1
        else:
            # print('skipping')
            # round_num += 1
            # i += 1
            num_fingers = int(input('How many fingers do you want to play?\n> '))


if player == num_wins:
    print('Player wins the game!')
elif computer == num_wins:
    print('Computer wins the game!')
