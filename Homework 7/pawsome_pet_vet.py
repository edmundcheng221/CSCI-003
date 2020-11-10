import animal_functions

def main():
    checked_in = [['edgrr allan pug', 'dog', 80], ['jane clawston', 'cat', 20], ['franze catka', 'cat', 60],
               ['bark twain', 'dog', 40]]
    lst = []
    while True:
        commands = input('check (i)n, check (o)ut, show (a)ll by name, (m)ost urgent, (l)east urgent, (f)ind by name, (q)uit\n> ')
        if commands == 'i':
            animal_name = input('What is the pet\'s name?\n> ')
            lst.append(animal_name)
            animal_type = input('What kind of animal is the pet?\n> ')
            lst.append(animal_type)
            urgency = input('How urgently does the pet need help (0-100)?\n> ')
            if urgency in range(0,101):
                lst.append(urgency)
            elif urgency not in range(0,101):
                urgency = input('Please enter (0-100)\n> ')
                lst.append(urgency)
            checked_in.append(lst)
            print(f'{animal_name} is checked in!')
            # print(checked_in)
        elif commands == 'o':
            for ele in enumerate(checked_in):
                print(str(ele[0]+1) + ' - ' + str(ele[1][0]) + ', ' + str(ele[1][1]))
            check_out = int(input('Please enter a number to check an animal out of the clinic\n> '))
            var = 1
            for update in enumerate(checked_in):
                if update[0] != check_out-1:
                    print(str(var) + ' - ' + str(update[1][0]) + ', ' + str(update[1][1]))
                    var += 1
        elif commands == 'a':
            order = animal_functions.sort_by_name(checked_in)
            print(order)
            for ordered in enumerate(order):
                print(str(ordered[0]+1) + ' - ' + str(ordered[1][0]) + ', ' + str(ordered[1][1]))
        elif commands == 'm':
            most = animal_functions.get_most_urgent(checked_in)
            print(f'{most[0]}, {most[1]} with urgency {most[2]}, should be seen right away!')

        elif commands == 'l':
            least = animal_functions.get_least_urgent((checked_in))
            print(least)
            print(f'{least[0]}, {least[1]} with urgency {least[2]}, can wait!')
        elif commands == 'f':
            animal = input('Please enter a name to search for\n> ')
            for search in checked_in:
                if animal == search[0]:
                    print(search)
                else:
                    print('None')
        elif commands == 'q':
            break

main()