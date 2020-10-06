"""
Homework #03
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-02

PWEASE GRADE EZ, I TRIED MY BEST
"""
print("Using while loops")
i = 0
while i < 30:
    i += 3
    if i % 4 == 0:
        pass
    else:
        print(i)
i = 33
while i > 0:
    i -= 3
    if i % 4 == 0:
        pass
    else:
        print(i)

print("Using for loops")
for i in range(0,33,3):
    if i % 3 == 0 and i % 4 != 0:
        print(i)
    else:
        pass
for i in range(30,0,-3):
    if i % 3 == 0 and i % 4 != 0:
        print(i)
    else:
        pass
