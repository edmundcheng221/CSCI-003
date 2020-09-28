"""
Homework #02
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-09-27

PWEASE GRADE EZ, I TRIED MY BEST
"""
import random
name = input('What is your name?')
character = input(name+" ,are you a warrior, wizard, or programmer?")
name_character = character + "" + name

if len(name) <= 15:
    print(".xX Welcome" + name + "Xx")
else:      # length of name is greater than 15
    print("Welcome" + character)

if character == "Programmer":
    print("There is no treasure here for you. The real treasure is the time spent programming.")
elif character == "Wizard" or character == "Warrior":
    # describe room
    print("You enter a room that looks like a room")
    print("You're in a dimly lit room, standing in front of an enormous steel chest.")
    open_close = input('Do you want to open the chest, run with the chest, or leave the room?')
    if open_close == "OPEN" or open_close == "Open" or open_close == "open":
        number = random.randint(1, 20)     # random number
        if number <= 5:  # no need to specify greater than 1 bc the random module is only from 1 to 20
            print("Something bad happens")
        elif 10 >= number >= 6:
            print("nothing interesting happens")
        elif 11 <= number <= 15:
            print("something good happens")
        else:  # all else numbers are greater than 15
            print("something great happens")
    elif open_close == "LEAVE" or open_close == "Leave" or open_close == "leave":
        print("Nothing happens")
    elif open_close == "run" or open_close == "RUN" or open_close == "Run":
        outside_destroy = input("Do you want to open the chest outside? or destroy it? or sell it?")
        if outside_destroy == "SELL" or outside_destroy == "sell" or outside_destroy ==  "Sell":
            print("Okay you can sell it for $50")
        elif outside_destroy == "DESTROY" or outside_destroy == "Destroy" or outside_destroy == "destroy":
            print("congrats you won, it was bat that was going to start the COVID pandemic!")

    else:
        print("You are scolded, GAME OVER")
else:
    print("Come back when you have a real job!")

