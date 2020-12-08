"""
Homework #11
CSCI-UA. 0003-001 Fall 2020
Edmund Cheng
ec3219
2020-12-06
"""


class AlphabetRange:
    def __init__(self, *args):
        length = len(args)
        if length == 1:
            self.start = 'A'
            self.step = 1
            self.end = args[0]
        elif length == 2:
            self.start = args[0]
            self.step = 1
            self.end = args[1]
        else:
            self.start = args[0]
            self.step = args[2]
            self.end = args[1]

    def __str__(self):
        return f'{self.start}' + "-" + f'{self.end}' + "," + f'{str(self.step)}'

    def __iter__(self):
        self.ele = self.start
        return self

    def __next__(self):
        current = self.ele
        if ord(current) >= ord(self.end):
            raise StopIteration
        else:
            self.ele = chr(ord(self.ele)+self.step)
            return str(current)

    def __eq__(self, other):
        if self.start == other.start and self.end == other.end and self.step == other.step:
            return True
        else:
            return False


if __name__ == '__main__':
    letters = AlphabetRange('D')
    print(letters)
    for letter in letters:
        print(letter)

    letters = AlphabetRange('B', 'E')
    print(letters)
    for letter in letters:
        print(letter)

    letters = AlphabetRange('C', 'L', 2)
    print(letters)
    for letter in letters:
        print(letter)

    letters1 = AlphabetRange('D')
    letters2 = AlphabetRange('A', 'D')
    print(letters1)
    print(letters2)
    print(letters1 == letters2)




