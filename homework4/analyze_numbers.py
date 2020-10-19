"""
Homework #04
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-14

"""


def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True


def is_abundant(num):
    fac_total = 0
    for f in range(2,num//2+1):
        if num%f==0:
            fac_total += f
        else:
            fac_total = fac_total + 0
    return fac_total > num


num = int(input('Please enter a number:\n> '))


if is_odd(num):
    print(f'{num} is odd')
else:
    print(f'{num} is not odd')

if is_prime(num):
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')

if is_abundant(num):
    print(f'{num} is abundant')
else:
    print(f'{num} is not abundant')