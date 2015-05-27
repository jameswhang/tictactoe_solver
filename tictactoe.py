def print_welcome_message():
    print "Welcome to the tictactoe player!"

board_array = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def display_board(board_array):
    print '---------------------'
    print '| ' + board_array[0] + '   |  ' + board_array[1] + '   |  ' + board_array[2] + '   |'
    print '|     |      |      |'
    print '---------------------'
    print '| ' + board_array[3] + '   |  ' + board_array[4] + '   |  ' + board_array[5] + '   |'
    print '|     |      |      |'
    print '---------------------'
    print '| ' + board_array[6] + '   |  ' + board_array[7] + '   |  ' + board_array[8] + '   |'
    print '|     |      |      |'
    print '---------------------'

def get_user_input():
    x = input('Type the x-coordinate of where you want to put your check (0 - 2): ')
    y = input('Type the y-coordinate of where you want to put your check (0 - 2): ')
    return [x, y]

def put_check(boardarray, userInput):
    boardarray[3*userInput[0]+userInput[1]] = 'x' 
    display_board(boardarray)

def convert_check_to_winner(check):
    assert(check == 'x' or check == 'o' or check == ' ')
    if check == 'x':
        return 'u'
    else:
        return 'c'

def determine_winner(b_array):
    if all_three_equal(b_array[0], b_array[1], b_array[2]):
        return convert_check_to_winner(b_array[0])
    elif all_three_equal(b_array[3], b_array[4], b_array[5]):
        return convert_check_to_winner(b_array[3])
    elif all_three_equal(b_array[6], b_array[7], b_array[8]):
        return convert_check_to_winner(b_array[6])
    elif all_three_equal(b_array[0], b_array[3], b_array[6]):
        return convert_check_to_winner(b_array[0])
    elif all_three_equal(b_array[1], b_array[4], b_array[7]):
        return convert_check_to_winner(b_array[1])
    elif all_three_equal(b_array[2], b_array[5], b_array[8]):
        return convert_check_to_winner(b_array[2])
    elif all_three_equal(b_array[0], b_array[4], b_array[8]):
        return convert_check_to_winner(b_array[0])
    elif all_three_equal(b_array[2], b_array[4], b_array[6]):
        return convert_check_to_winner(b_array[2])
    else:
        return 'd'

def all_three_equal(a, b, c):
    if a is ' ' or b is ' ' or c is ' ':
        return False
    return a == c and a == b;

def main():
    print_welcome_message()
    display_board(board_array)

    winner_decided = False

    while winner_decided == False:
       userInput = get_user_input()
       put_check(board_array, userInput)

if  __name__ == "__main__":
    main()
