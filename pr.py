import random

def ascii_name_plaque(name):
    """
    (str) -> str
    precondition: name must be in quotations
    Takes a string of input and forms a decorative ASCII art plaque around it.
    >>>ascii_name_plaque("adam")
    **************
    *            *
    *  __adam__  *
    *            *
    **************
    """
    a = len(name)
    b = a + 6
    c = str(name)
    print(("*" * b) + 4 * "*")
    print("*" + " " * (b + 2) + "*")
    print("*" + "  " + "__" + c + "__" + "  " + ("*"))
    print("*" + " " * (b + 2) + "*")
    print(("*" * b) + 4 * "*")
    return None


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''
    random.shuffle(deck)
    print("Shuffling the deck")
    return deck


def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None] * size

    letter = 'A'
    for i in range(len(board) // 2):
        board[i] = letter
        board[i + len(board) // 2] = board[i]
        letter = chr(ord(letter) + 1)
    return shuffle_deck(board)


def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i + 1)), end=' ')
    


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()


def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    temp_list = discovered[:]
    if original_board[p1] != original_board[p2]:
        temp_list = discovered[:]
        temp_list[p1] = original_board[p1]
        temp_list[p2] = original_board[p2]
        print_board(temp_list)
    if original_board[p1] == original_board[p2]:
        discovered[p1] = original_board[p1]
        discovered[p2] = original_board[p2]
        print_board(discovered)
    


#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file.
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i] = raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str
    The functions takes as input a list of strings representing a deck of cards.
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    board = []

    for item in l:
        if item != "*":
            board.append(item)
    for item in l:
        if board.count(item) % 2 != 0 or board.count(item) == 1:
            pos = board.index(item)
            del board[pos]
    return board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.
    Precondition: Every element in the list appears even number of times
    '''

    for item in l:
        if l.count(item) > 2:
            return ascii_name_plaque("This deck is now playable but not rigorous and it has " + str(len(l)) + " cards")
    else:
        return ascii_name_plaque("This deck is now playable and rigorous and it has " + str(len(l)) + " cards")


####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")
    original_board = board
    discovered = board[:]
    count = 0
    if len(board) == 0:
        return print(("The resulting board is empty. \n playing concentration game with an empty board is impossible. \n Goodbye."))
    for i in range(0, len(discovered)):
        discovered[i] = "*"
    print_board(discovered)
    while discovered != original_board:
        print("\n")
        print("Enter Two distinct positions on the board you want to be revealed")
        print("i.e two integers in the range [1," + str(len(board)) + "]")
        p1 = (int(input("Enter position 1: "))-1)
        p2 = (int(input("Enter position 2: "))-1)
        if (p1 +1) > len(original_board) or (p1 +1) < 1 or (p2 + 1) > len(original_board) or (p2 + 1) < 1:
            print("That is not a valid option \n ")
            print("Enter Two distinct positions on the board you want to be revealed")
            print("i.e two integers in the range [1," + str(len(board)) + "]")
            p1 = (int(input("Enter position 1: "))-1)
            p2 = (int(input("Enter position 2: "))-1)
        if p1 == p2:
            print("One or both of your chosen positions has already been paired \n")
            print("You chose the same positions")
            print("Please try again. This guess did not count. Your current number of guesses is " + str(count))
            input("\nPress enter to continue. ")
            print("\n" * 50)
            continue
        if discovered[p1] != "*" or discovered[p2] != "*":
            print("One or both of your chosen positions has already been paired \n")
            print("Please try again. This guess did not count. Your current number of guesses is " + str(count))
            input("\nPress enter to continue. ")
            print("\n" * 50)
            continue
        print_revealed(discovered,p1,p2,original_board)
        input("\nPress enter to continue. ")
        print("\n" * 50)
        count += 1
    best = str(count - int(len(board)/2))
    print(" Congratulations! you completed the game with " + str(count) + " guesses. That is " + best + " more than the best possible")
    
    # this is the funciton that plays the game
    # YOUR CODE GOES HERE


def type_of_game():
    ascii_name_plaque("Welcome to my concentration game")
    typeg = int(input(
        "Would you like (enter 1 or 2 to indicate your choice) \n (1) me to generate a rigorous deck for you \n (2) or, would you like me to read a deck from a file?"))
    while typeg != 1 and typeg != 2:
        print(str(typeg) + " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice \n")
        typeg = int(input())
    while (typeg == 1):
        size = int(input("How many card do you want to play with? \n enter an even number in between 0 and 52"))
        if (size >= 0 and size <= 52) and (size % 2) == 0:
            board = create_board(size)
            input("\nPress enter to continue. ")
            print("\n" * 50)
            play_game(board)
            break
    if typeg == 2:
        file = input("Enter the name of the file: ")
        file = file.strip()
        board = read_raw_board(file)
        board = clean_up_board(board)
        is_rigorous(board)
        input(" \n press enter to continue")
        print("\n" * 40)
        play_game(board)

        # board=clean_up_board(board)
        # YOUR CODE FOR OPTION 1 GOES HERE
        # In option 1 somewhere you need to and MUST have a call like this:
        # board=create_board(size)

        # YOUR CODE FOR OPTION 2 GOES HERE
        # In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
        #
        # print("You chose to load a deck of cards from a file")
        # file=input("Enter the name of the file: ")
        # file=file.strip()
        # board=read_raw_board(file)
        # board=clean_up_board(board)'''

type_of_game()