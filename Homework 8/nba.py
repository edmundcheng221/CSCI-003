"""
Homework #08
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-15
"""


with open('stats-clean.txt', 'r') as stats:
    percentage = ''  # filler
    for player in stats:
        item = player.strip().split(",")
        test = 0
        try:
            test = float(item[-2])/float(item[-1])
            if test >= 0.5:
                percentage += item[0] + ', ' + str(format(float(item[-2])/float(item[-1]),'.2f'))
                percentage += '\n'
        except ValueError:
            pass
        except ZeroDivisionError:
            # percentage = 0.0
            pass
        print(percentage)

        with open('report.csv', 'w') as report:
            report.write(percentage)
