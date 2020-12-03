"""
Homework #10
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-25
"""
from stack import Stack


class RPNCalculator:
    def __init__(self, expression):
        self.expression = expression
        self.stack = Stack()

    def evaluate(self):
        chars = self.expression.split(" ")

        for ele in chars:
            if ele.isnumeric():
                self.stack.push(int(ele))
            # I will use '^' as the symbol of exponent instead of '**' since I want only one character
            elif ele == '+' or ele == '-' or ele == '*' or ele == '/' or ele == '^':
                operator1 = self.stack.pop()
                operator2 = self.stack.pop()
                if ele == '+':
                    self.stack.push(operator2 + operator1)
                elif ele == '-':
                    self.stack.push(operator2 - operator1)
                elif ele == '*':
                    self.stack.push(operator2 * operator1)
                elif ele == '/':
                    self.stack.push(operator2 / operator1)
                elif ele == '^':
                    self.stack.push(operator2 ** operator1)
                elif ele == ' ':
                    pass
                else: # for characters that are not numeric or operators such as '?'
                    pass

        if len(self.stack) == 1:
            return self.stack.pop()
        return None


if __name__ == '__main__':
    c = RPNCalculator('2 3 * 4 +')
    print(c.expression)  # '2 3 * 4 +'
    c.evaluate() # 10


