"""
Homework #04
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-14

"""

# Part 1


def horizontal_line(char, width, left_padding):
    s = ''
    s += ' ' * left_padding + char * width
    return s


def vertical_lines(char, height, left_padding, number, interior_offset):
    s = ""
    for row_num in range(height):
        row = ""
        row += " " * left_padding
        for col_num in range(number):
            space_between = " " * interior_offset
            row += char + space_between
        row += "\n"
        s += row
    return s


def vertical_line(char, height, left_padding):
    s = ''
    for i in range(height):
        s += left_padding * ' ' + char + '\n'
    return s


# Part 2


def print_zero(char, width):
    if width < 3:
        width = 3
    s = ''
    s = s + horizontal_line(char, width, 0)+"\n"
    s = s + vertical_lines(char, 3, 0, 2, width-2)
    s = s + horizontal_line(char, width, 0)+"\n"
    # print(s)
    return s


def print_one(char, width):
    if width < 3:
        width = 3
    s = ""
    s += vertical_line(char, 5, width-1)
    # print(s)
    return s


def print_two(char, width):
    if width < 3:
        width = 3
    s = ''
    s += horizontal_line(char, width, 0) + '\n'
    s += horizontal_line(char, 1, width-1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += horizontal_line(char, 1, 0) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    # print(s)
    return s


def print_three(char, width):
    if width < 3:
        width = 3
    s = ''
    s += horizontal_line(char, width, 0) + '\n'
    s += horizontal_line(char, 1, width-1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += horizontal_line(char, 1, width-1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    # print(s)
    return s


def print_four(char, width):
    if width < 3:
        width = 3
    s = ''
    s += vertical_lines(char, 2, 0, 2, width-2)
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 2, width-1)
    # print(s)
    return s


def print_five(char, width):
    if width < 3:
        width = 3
    s = ''
    s += horizontal_line(char, width, 0) + '\n'
    s += horizontal_line(char, 1, 0) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += horizontal_line(char, 1, width-1) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    # print(s)
    return s


def print_six(char, width):
    if width < 3:
        width = 3
    s = ''
    s += horizontal_line(char, width, 0) + '\n'
    s += horizontal_line(char, 1, 0) + '\n'
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 1, 0, 2, width-2)
    s += horizontal_line(char, width, 0) + '\n'
    # print(s)
    return s


def print_seven(char, width):
    if width < 3:
        width = 3
    s = ''
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 4, width-1)
    # print(s)
    return s


def print_eight(char, width):
    if width < 3:
        width = 3
    s = ''
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 1, 0, 2, width-2)
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 1, 0, 2, width-2)
    s += horizontal_line(char, width, 0) + '\n'
    # print(s)
    return s


def print_nine(char, width):
    if width < 3:
        width = 3
    s = ''
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_lines(char, 1, 0, 2, width-2)
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 2, width-1)
    # print(s)
    return s


def print_plus(char, width):
    if width < 3:
        width = 3
    s = ''
    s += vertical_line(char, 2, width-3)
    s += horizontal_line(char, width, 0) + '\n'
    s += vertical_line(char, 2, width-3) + '\n'
    # print(s)
    return s


def print_minus(char, width):
    if width < 3:
        width = 3
    s = ''
    s += vertical_line('', 1, width)
    s += horizontal_line(char, width, 0)+'\n'
    # print(s)
    return s


# Part 3


def check_answer(left, right, answer, operator):
    if operator == '-':
        ans = left - right
    elif operator == '*':
        ans = left * right
    else:
        ans = left + right
    return ans == answer


if __name__ == '__main__':
    print(print_zero('*',5))
    print(print_one('*',5))
    print(print_two('*',5))
    print(print_three('*',5))
    print(print_four('*',5))
    print(print_five('*',5))
    print(print_six('*',5))
    print(print_seven('*',5))
    print(print_eight('*',5))
    print(print_nine('*',5))
    print(print_plus('*',5))
    print(print_minus('*',5))
    print(check_answer(5, 3, 2, '+'))
    print(check_answer(5, 3, 15, '*')) # Returns true

########
# I did the extra credit

########




