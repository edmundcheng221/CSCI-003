"""
Homework #08
CSCI-UA.003-001 Fall 2020
Edmund Cheng
ec3219
2020-11-15
"""

# I can't seem to get the output, but the logic is there. I put comments (please gib partial credit)


def find_words(words, f):
    found_words = [] # empty list of found words to populate later
    temp_lst = list(words)  # list of letters in string ex: ['d', 'i', 'r', 't'] to allow iteration and removal of
    # each letter
    with open("enable1.txt", "r") as f: # open the file to read
        for line in f: # iterate trough each line
            item = line.strip().split("\n")  # remove white space, and turn to list with split function
            for word in item: # iterate though each word in list of words
                # print(word)
                found = True   # set to true
                for ch in word:     # iterate through each character
                    # print(type(ch))
                    if ch in temp_lst:   # if character is in the temporary list
                        # found = True
                        temp_lst.remove(ch)    # remove the letter in the temp list so we can't reuse it
                        # print(temp_lst)
                    elif ch not in temp_lst:  # if its not in the list,
                        found = False   # we set the found to false and we know that that word can not be made with our
                        # letters
                if found:  # if we get true, it means we can make the word
                    found_words.append(word)   # we add it to the empty list defined earlier
                # repeat this process for all words
            return found_words  # return all the words from the dictionary that can be made


def main(): # main function
    letters = input("Give me a set of letters between 1 and 7.\n> ")  # user input for the letters
    while not letters.isalpha() or len(letters) < 1 or len(letters) > 7:    # we want only letters and the length to be
        # between 1 and 7 characters
        letters = input("Give me a set of letters between 1 and 7.\n> ")   # we continually ask if requirements not met
    try: # shows only max number of words
        max_words = int(input("What is the maximum number of words to display?\n> "))   # ask for max words
        dictionary = open("enable1.txt", "r")
        desired_words = find_words(letters, dictionary)
        desired_words.sort() # sort in alphabetical order
        print(f'Showing max {max_words} results')
        print(desired_words[0:max_words])
    except ValueError:  # shows all the words
        # if we don't get a number in the try block
        dictionary = open("enable1.txt", "r")
        desired_words = find_words(letters, dictionary)
        desired_words.sort()
        print(f'Showing all results')
        print(desired_words)


if __name__ == "__main__":
    main() # call main function
    diction = open("enable1.txt", "r")  # open dictionary text file as read
    find_words('dirt', diction)   # set parameters for the function



