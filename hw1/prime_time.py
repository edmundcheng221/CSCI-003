
"""
Homework #01
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-09-14

"""
print('Part 1')
num = int(input('Give me a whole number'))
print('> ', num)
print(str(num)+' * 3 = ', num*3)
print(str(num)+' * 5 = ', num*5)
print(str(num)+' * 7 = ', num*7)
print(str(num)+' * 11 = ', num*11)
print(str(num)+' * 127 = ', num*127)

print('Part 2')
num = int(input('Give me a whole number'))
print('> ', num)
str1 = str(num)+' * 3'
prod1 = str(num*3)
str2 = str(num)+' * 5'
prod2 = str(num*5)
str3 = str(num)+' * 7'
prod3 = str(num*7)
str4 = str(num)+' * 11'
prod4 = str(num*11)
str5 = str(num)+' * 127'
prod5 = str(num*127)
print(format(str1, '<9'),'=', format(prod1, '>5'))
print(format(str2, '<9'),'=', format(prod2, '>5'))
print(format(str3, '<9'),'=', format(prod3, '>5'))
print(format(str4, '<9'),'=', format(prod4, '>5'))
print(format(str5, '<9'),'=', format(prod5, '>5'))

print('Part 3')
num = int(input('Give me a whole number'))

print('> ' + str(num))
format_string = '>' + str(len(str(num*127))) # find the length of the largest product/result to determine spacing
# print(format_string)
str1 = str(num)+' * 3'
prod1 = str(int(num)*3)
str2 = str(num)+' * 5'
prod2 = str(int(num)*5)
str3 = str(num)+' * 7'
prod3 = str(int(num)*7)
str4 = str(num)+' * 11'
prod4 = str(int(num)*11)
str5 = str(num)+' * 127'
prod5 = str(int(num)*127)

print(format(str1, '<9'),'=', format(prod1, format_string)) # use the max length to format results
print(format(str2, '<9'),'=', format(prod2, format_string))
print(format(str3, '<9'),'=', format(prod3, format_string))
print(format(str4, '<9'),'=', format(prod4, format_string))
print(format(str5, '<9'),'=', format(prod5, format_string))



