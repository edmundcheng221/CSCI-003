"""
Homework #10
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-25
"""


class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        str_data = ""
        for i in self.data:
            str_data = "|" + str(i) + "|" + "\n" + str_data
        str_data += " ‾"
        return str_data

    def empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def peek(self):
        if self.empty():
            return -1
        return self.data[-1]

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if self.empty():
            return -1
        return self.data.pop()

    def __len__(self):  # use this magic method to find the length to determine whether length is 1
        return len(self.data)


if __name__ == '__main__':
    s = Stack()
    print(s.empty()) # True
    s.push(1)
    print(s.empty()) # False
    s.push(2)
    s.push(3)
    print(s.peek()) # 3
    print(s.pop()) # 3
    print(s.peek()) # 2
    print(s)