def flattened(lst):
    new_lst = []
    for i in lst:
        for ele in i:
            new_lst.append(ele)
    return new_lst


def shift_left(lst, n, fill_value = 0):
    lst[:] = lst[n:]
    lst.extend([fill_value] * n)
    return lst


def shifted_left(lst, n, fill_value=0):
    answer = []
    for i in range(n, len(lst)):
        answer.append(lst[i])

    left = len(lst) - len(answer)
    for i in range(left):
        answer.append(fill_value)
    return answer


def shift_right(lst, n, fill_value=0):
    answer = []
    for i in range(0, len(lst) - n):
        answer.append(lst[i]);

    left = len(lst) - len(answer)
    for i in range(left):
        answer.insert(0, fill_value)

    for i in range(0, len(lst)):
        lst[i] = answer[i]


def shifted_right(lst, n, fill_value=0):
    size = len(lst)
    if n >= size:
        fill_in_place(lst, fill_value)
        return lst
    else:
        emp_list1 = []
        for i in range(0, n):
            emp_list1.append(fill_value)
            size_left = size - n
        for i in range(0, size_left):
            emp_list1.append(lst[i])
        return emp_list1


def fill_in_place(lst, fill_value=0):
    length = len(lst)
    lst.clear()
    for i in range(0, length):
        lst.append(fill_value)


def truncate_long_words(words, n):
    new_words = []
    [new_words.append(words[i][0:n]) for i in range(len(words)) if len(words[i]) > n]
    return new_words


def sum_postive_pairs(lst):
    result = [x+y for x,y in lst if x > 0 and y > 0]
    return result


def consecutive_chars(start_ch, end_ch):
    result = [" " if(len(start_ch)!=1 or len(end_ch)!=1) or ord(end_ch)<=ord(start_ch) else [chr(x) for x in range(ord(start_ch),ord(end_ch)+1)]]
    a = "".join(result[0])
    return a


def unique(*lsts):
    result= [x for y in lsts for x in y]
    return set(result)


if __name__ == '__main__':
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = flattened(nested)
    print(flat)  # --> [1, 2, 3, 4. 5, 6]

    numbers = [1, 2, 3, 4]
    shift_left(numbers, 2)
    print(numbers)

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_left(numbers, 2)
    print(shifted_numbers)

    numbers = [1, 2, 3, 4]
    shift_right(numbers, 2)
    print(numbers)

    numbers = [1, 2, 3, 4]
    shifted_numbers = shifted_right(numbers, 2)
    print(shifted_numbers)


    list1 = [1, 2, 3, 4]
    fill_in_place(list1)
    print(list1)

    print(truncate_long_words(['aardvark', 'bison', 'chameleon'], 5))
    # ['aardv...', 'chame...']

    print(sum_postive_pairs([(1, 2), (3, 4)]))
    print(sum_postive_pairs([(1, 3), (3, 6)]))
    print(sum_postive_pairs([(1, 12), (4, 4)]))
    print(sum_postive_pairs([(1, -12), (4, 4)])) # since the first tuple has a negative, we on;y get the sum of the second

    print(consecutive_chars('A', 'Z'))
    print(consecutive_chars('x', 'z'))  # xyz
    print(consecutive_chars('Z', 'Z'))  # ''
    print(consecutive_chars('Z', 'A'))  # ''
    print(consecutive_chars('AAA', 'Z'))  # ''

    print(unique([1, 2, 3], [2, 3, 4], [3, 4, 5]))
    print(unique([1, 2, 3], [2, 3, 4], [3, 4, 5], [7, 1, 8]))
