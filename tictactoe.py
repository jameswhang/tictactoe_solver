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
    boardarray[3*userInput[0]+userInput[1]] = 'O' 
    display_board(boardarray)

def main():
    print_welcome_message()
    display_board(board_array)
    userInput = get_user_input()
    put_check(board_array, userInput)

if  __name__ == "__main__":
    main()
