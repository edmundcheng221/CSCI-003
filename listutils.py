"""
Homework #06
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-01

"""
import random


def get_duplicates(lst):
    new_list = []
    for i in lst:
        if lst.count(i) >= 2:
            new_list.append(i)
    return list(set(new_list))


def has_duplicates(lst):
    for i in lst:
        if lst.count(i) >= 2:
            return True
        else:
            return False


def join_elements_with(glue, lst):
    new_str = ""
    counter = 0
    for i in lst:
        counter += 1
        if counter < len(lst):
            new_str += i + glue
        else:
            new_str += i
    return new_str


def fill(size, fill_value = 0):
    lst = []
    counter = 0
    while counter < size:
        lst.append(fill_value)
        counter += 1
    return lst


def random_choose(lst):
    a = random.randint(0, len(lst) - 1)
    new = lst[a]
    return new


def random_fill(min_val, max_val, list_length):
    counter = 0
    list = []
    while counter < list_length:
        counter += 1
        a = random.randint(min_val, max_val)
        list.append(a)
    return list


def stringify_elements(lst):
    new_list = []
    for i in lst:
        new_list.append(str(i))
    return new_list


def mean(lst):
    sum = 0
    for i in lst:
        sum += i
    mean = sum / len(lst)
    return mean