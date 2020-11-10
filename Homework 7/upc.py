def generate_bar_widths(s):
    result = ''
    new = ''
    zero = '3211'
    one = '2221'
    two = '2122'
    three = '1411'
    four = '1132'
    five = '1231'
    six = '1114'
    seven = '1312'
    eight = '1213'
    nine = '3112'
    beginning = '111'
    middle = '11111'
    end = '111'
    result += beginning
    for i in range(len(s)):
        if s[i] == '0':
            result += zero
        elif s[i] == '1':
            result += one
        elif s[i] == '2':
            result += two
        elif s[i] == '3':
            result += three
        elif s[i] == '4':
            result += four
        elif s[i] == '5':
            result += five
        elif s[i] == '6':
            result += six
        elif s[i] == '7':
            result += seven
        elif s[i] == '8':
            result += eight
        elif s[i] == '9':
            result += nine
    result += end
    for j in range(len(result)//2):
        new += result[j]
    new += middle
    for k in range(len(result)//2, len(result)):
        new += result[k]

    return new


assert generate_bar_widths('043000181706') == '11132111132141132113211321111111222112132221131232111114111', "wrong"


def valid_barcode(s):
    sum_odd = 0
    pos = 0
    length = len(s)
    while length > 0:
        if pos % 2 == 1:
            sum_odd += int(s[pos])
            pos += 1
            length -= 1
        else:
            pos += 1
            length -= 1

    sum_even = 0
    pos_even = 0
    length_even = len(s)
    while length_even > 0:
        if pos_even % 2 == 0:
            sum_even += int(s[pos_even])
            pos_even += 1
            length_even -= 1
        else:
            pos_even += 1
            length_even -= 1

    check = 10-(((sum_odd * 3) + sum_even) % 10)
    # print(check)
    if len(s) != 12 or int(s[-1]) != check:
        return False
    else:
        return True


if __name__ == '__main__':
    print(generate_bar_widths('043000181706'))

    print(valid_barcode('036000291452'))  # --> True
    print(valid_barcode('036000291450'))  # --> False
    print(valid_barcode('075678164125'))  # --> False
    print(valid_barcode(''))  # --> False

