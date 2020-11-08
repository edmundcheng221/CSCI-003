"""
Homework #06
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-01

"""
import random


def is_valid_month_num(n):
    if n in range(1, 13):
        return True
    else:
        return False


assert is_valid_month_num(3) == True, "3 is a within the valid range"
assert is_valid_month_num(37) == False, "37 is not within the valid range"


def month_num_to_string(month_num):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    if is_valid_month_num(month_num):
        return months[month_num - 1]
    else:
        return None


assert month_num_to_string(1) == 'January', "1 corresponds to Jan"
assert month_num_to_string(10) == 'October', '10 corresponds to October'
assert month_num_to_string(234) is None, 'There is no month for this value'


def date_to_string(date_list):
    month = month_num_to_string(date_list[1])
    day = date_list[2]
    year = date_list[0]
    date_to_string = str(month) + ' ' + str(day) + ',' + ' ' + str(year)
    return date_to_string


assert date_to_string([1979, 10, 7]) == 'October 7, 1979', "Conversion not correct"


def dates_to_strings(list_of_date_lists):
    new_list = []
    for i in range(len(list_of_date_lists)):
        result = date_to_string(list_of_date_lists[i])
        new_list.append(result)
    return new_list


assert dates_to_strings([[1979, 10, 7], [2000, 2, 20]]) == ['October 7, 1979', 'February 20, 2000'], "Conversion is " \
                                                                                                     "not correct"


def remove_years(list_of_date_lists):
    new_list = []
    for i in range(len(list_of_date_lists)):
        result = list_of_date_lists[i][1:]
        new_list.append(result)
    return new_list


assert remove_years([[1979, 10, 7], [2000, 2, 20]]) == [[10, 7], [2, 20]], "conversion is not correct"


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False


assert is_leap_year(1992) == True, "Incorrect answer, supposed to be true"
assert is_leap_year(2000) == True, "Incorrect answer, supposed to be true"
assert is_leap_year(1900) == False, "Incorrect answer, supposed to be false"


def get_num_days_in_month(month_num, year):
    num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # default
    if is_leap_year(year):
        num_days[1] = 29
    if not is_valid_month_num(month_num):
        # print(None)
        return None
    else:
        # print(num_days[month_num-1])
        return num_days[month_num-1]


def generate_date(start_year, end_year):
    year = random.randint(start_year, end_year)
    month = random.randint(1,12)
    day = random.randint(1, get_num_days_in_month(month, year))
    date_full = [year, month, day]
    # print(date_full)
    return date_full


if __name__ == '__main__':
    result1 = is_valid_month_num(3)
    print(result1)  # True
    result2 = is_valid_month_num(37)
    print(result2)  # False

    result1 = month_num_to_string(1)
    print(result1)  # 'January'
    result2 = month_num_to_string(10)
    print(result2)  # 'October'
    result3 = month_num_to_string(234)
    print(result3)  # None

    date_to_string([1979, 10, 7])
    # returns the string: October 7, 1979

    res = dates_to_strings([[1979, 10, 7], [2000, 2, 20]])
    print(res)  # ['October 7, 1979', 'February 20, 2000']

    res = remove_years([[1979, 10, 7], [2000, 2, 20]])
    print(res)  # [[10, 7], [2, 20]]

    for year in [1988, 1992, 1996, 1600, 2000, 2400]:
        print(is_leap_year(year))  # True for each one!

    for year in [1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600]:
        print(is_leap_year(year))  # False for each one!

    get_num_days_in_month(2, 1988)  # 29
    get_num_days_in_month(2, 1900)  # 28
    get_num_days_in_month(11, 1900)  # 30
    get_num_days_in_month(12, 1900)  # 31
    get_num_days_in_month(1, 1900)  # 31
    get_num_days_in_month(30, 1999)  # None

    date = generate_date(2015, 2017)
    print(date)  # a random 3 element list, like: [2017, 9, 5]