def find_by_name(name, animals):
    for i in animals:
        if name == i[0]:
            return i
        else:
            return None


def stringify_animals(animals):
    whole_list = ""
    animal_list = []
    counter = 0
    for i in animals:
        counter += 1
        name_kind = str(counter) + " - " + i[0] + ", " + i[1]
        animal_list.append(name_kind)
    for a in animal_list:
        whole_list += (a + "\n")
    return whole_list


def get_most_urgent(animals):
    urgent = []
    urgency = 0
    for i in animals:
        if i[2] > urgency:
            urgency = i[2]
            urgent.append(i)
        else:
            continue
    return urgent[-1]


def get_least_urgent(animals):  # I only wrote this function because it would help me for the pawsome_pet_vet hw problem
    urgent = []
    urgency = 100
    for i in animals:
        if i[2] <= urgency:
            urgency = i[2]
            urgent.append(i)
        else:
            continue
    return urgent[-1]


def sort_by_name(List):
    n = len(List)
    swap = True
    while (swap):
        swap = False
        for i in range(n - 1):
            if List[i][0] > List[i + 1][0]:
                List[i], List[i + 1] = List[i + 1], List[i]
                swap = True
    return List


if __name__ == '__main__':
    animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
    res = find_by_name('sam', animal_list)
    print(res)  # ['sam', 'snake', 4]

    animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
    res = stringify_animals(animal_list)
    print(res)

    animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
    print(get_most_urgent(animal_list))


    animal_list = [['edgrr allan pug', 'dog', 80], ['jane clawston', 'cat', 20], ['franze catka', 'cat', 60],
                  ['bark twain', 'dog', 40]]
    print(get_least_urgent(animal_list))

    animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
    sorted_animal_list = sort_by_name(animal_list)
    print(sorted_animal_list)