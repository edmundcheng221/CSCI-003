"""
Homework #03
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-10-02

PWEASE GRADE EZ, I TRIED MY BEST
"""

is_false = False # loop controller
while is_false != True: # we want a positive integer. While loop checks for that.
    num = int(input("Enter the height of your pyramid: "))
    if num >= 0:
        is_false = True
    else:
        is_false = False
def string(i):
    s = ""
    if i <10: # spacing for double digits
        s = " " # adds space
    return s + str(i)
all_rows = ""
for j in range(1,num+2):
    row = " "*3*(num-j+1) #spaces
    for i in range(j-1,1,-1): # from j-1, to 1 with step size 1
        s = string(i)         # counts backwards by 1
        row+=s + " "
    for i in range(1,j,1):      # from 1 to j with step size 1
        s = string(i)              # counts forward by 1
        row+=s + " "
    row +="\n"         # new line
    all_rows += row          # adds row
print(all_rows)