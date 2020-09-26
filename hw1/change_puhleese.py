"""
Homework #01
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-09-14

"""
item_name1 = input('What is the name of the first item?:')
print('> ', item_name1)
item_price1 = float(input('How much does the first item cost?: '))
print('> ', item_price1)
item_quantity1 = int(input('How many are being purchased?: '))
print('> ', item_quantity1)
item_name2 = input('What is the name of the second item?: ')
print('> ', item_name2)
item_price2 = float(input('How much does the second item cost?: '))
print('> ', item_price2)
item_quantity2 = int(input('How many are being purchased?: '))
print('> ', item_quantity2)
item_name3 = input('What is the name of the third item?: ')
print('> ', item_name3)
item_price3 = float(input('How much does the third item cost?: '))
print('> ', item_price3)
item_quantity3 = int(input('How many are being purchased?: '))
print('> ', item_quantity3)
amount_paid = float(input('How many was paid?: '))
print('> ', amount_paid)
# max width is 80 characters
string_title = 'PREMIER PYTHON PLAZA RECEIPT' # title of receipt
print(format(string_title, '>'+str(40+len(string_title)//2)))   # title with formatting so that it is in the center
print('='*80)  # 80 equal signs
prod1 = str(format(item_price1*item_quantity1,'.2f')) # string of the product of the first item and its quantity
prod2 = str(format(item_price2*item_quantity2, '.2f')) # string of the product of the second item and its quantity
prod3 = str(format(item_price3*item_quantity3,'.2f')) # string of the product of the third item and its quantity
info1 = str(item_quantity1) + ' x ' + item_name1   # text with information about the item and quantity (item1)
info2 = str(item_quantity2) + ' x ' + item_name2 # text with information about the item and quantity (item2)
info3 = str(item_quantity3) + ' x ' + item_name3 # text with information about the item and quantity (item3)
print(info1, format('$'+prod1, '>'+str(79-len(info1))))     # cost of item 1 (taking into account quantity)
print(info2, format('$'+prod2, '>'+str(79-len(info2))))     # cost of item 2 (taking into account quantity)
print(info3, format('$'+prod3, '>'+str(79-len(info3))))     # cost of item 3 (taking into account quantity)
print('='*80) # 80 equal signs
net_cost = str(float(prod1)+float(prod2)+float(prod3))       # net cost of the transaction changed into string data
sales_tax = str(format(float(net_cost) * 0.08875,'.2f'))   # string of sales tax amount for this transaction
amount_owed = str(format(float(net_cost) + float(sales_tax),'.2f')) # string data for the total amount owed
amount_paid_str = str(format(amount_paid, '.2f'))    # string data for the amount paid
change = str(format(amount_paid - float(amount_owed),'.2f'))   # string data for the change due
text1 = 'TOTAL COST OF ITEMS'
text2 = 'SALES TAX'
text3 = 'AMOUNT OWED'
text4 = 'AMOUNT PAID'
text5 = 'CHANGE'
print(text1, format('$'+net_cost,'>'+str(79-len(text1))))    # total cost on items line in the table (formatted)
print(text2, format('$'+sales_tax,'>'+str(79-len(text2))))       # sales tax on items line in the table (formatted)
print(text3, format('$'+amount_owed,'>'+str(79-len(text3))))   # amount owed on items line in the table (formatted)
print(text4, format('$'+amount_paid_str,'>'+str(79-len(text4))))    # amount paid on items line in the table (formatted)
print(text5, format('$'+change,'>'+str(79-len(text5))))    # change due on items line in the table (formatted)
print('='*80)  # row of =
print('CHANGE:')
change_cents = int(float(change)*100)  # the change converted to coins
old_change_cents = change_cents       # store the initial number of change in cents so that we can reuse later
count = 0
while change_cents >= 25:               #while loop determines how many quarters are needed
    change_cents = change_cents - 25
    count += 1
print(str(count) + ' x ' + 'quarters')
remainder_after_quarters = old_change_cents - count*25
count2 = 0
old_remainder_after_quarters = remainder_after_quarters
while remainder_after_quarters >= 10:              # while loop determines how many dimes are needed
    remainder_after_quarters = remainder_after_quarters - 10
    count2 += 1
print(str(count2) + ' x ' + 'dimes')
remainder_after_dimes = old_remainder_after_quarters - count2*10
old_remainder_after_dimes = remainder_after_dimes
count3 = 0
while remainder_after_dimes >= 5:                 # while loop determines the number of nickels needed
    remainder_after_dimes = remainder_after_dimes - 5
    count3 += 1
print(str(count3)+' x '+'nickels')
remainder_after_nickels = old_remainder_after_dimes - count3*5

count4 = 0
while remainder_after_nickels >= 1:                # while loop determines the number of pennies needed
    remainder_after_nickels = remainder_after_nickels - 1
    count4 += 1
print(str(count4)+' x '+'pennies')










