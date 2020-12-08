"""
Homework #11
CSCI-UA. 0003-001 Fall 2020
Edmund Cheng
ec3219
2020-12-06
"""


def count_nested_tuple(t):
    count = 0
    for ele in t:
        if type(ele) is tuple:
            count += count_nested_tuple(ele)
        else:
            count += 1
    return count


if __name__ == '__main__':
    empty = tuple()
    print(count_nested_tuple(empty))
    print(count_nested_tuple((1,)))
    print(count_nested_tuple((1, 2)))
    print(count_nested_tuple((1, (2, 3))))
    print(count_nested_tuple((1, (2, 3), 4)))
    print(count_nested_tuple((1, (2, 3, (4, 5)))))
    print(count_nested_tuple((1, (2, 3, (4, 5), 6))))