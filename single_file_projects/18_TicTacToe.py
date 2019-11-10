import random
from itertools import cycle
from pyfiglet import Figlet

def select_random_player():
    ''' selects randomly a player to start the game '''
    players = [name1, name2]
    player1_name = random.choice(players)
    
    if player1_name == name1:
        player2_name = name2
    else:
        player2_name = name1
        
    print(player1_name + " will start the game!")
    return player1_name, player2_name

def sign_assignment():
    ''' lets the first player to choose the sign and base on that it assigns the appropriate signs to the 1st and 2nd player '''
    while True:
        try:
            player1_sign = (str(input("Please choose O or X: "))).upper()
            if player1_sign in ("O", "X"):
                break
        except ValueError:
            print("The only valid inputs are O or X!")
        finally:
            print("The only valid inputs are O or X!")

    if player1_sign == "O":
        player2_sign = "X"
    else:
        player2_sign = "O"                                                       
        player1_sign = "X"
    return player1_sign, player2_sign

def display_board(game_map, player=0, row=0, column=0, just_display =False):
    '''needs: game_map - the current board, player = sign of player , row, column - were to put the sign on the board, (just_display = show the currently 
    played board). Base on the input of coordinates from the player it insert the sign into the indicated place, but before that it checks if the place
    is not alreay occupied. In case of Value Exception it informs about the error and ask for the correct error. ''' 
    print("     0     1     2")
    if not just_display: 
        board[row][column] = player
    for count, row in enumerate(game_map):
        print(count,row)
    return game_map, True   

def win(current_game):
    '''Conditions to win the game'''
    # Horizontal
    for h_line in board:
        col1 = h_line[0]
        col2 = h_line[1]
        col3 = h_line[2]
        if col1 == col2 == col3 != "_":
            if col1 == "O":
                print(("{0}, you won!").format(player1_name))
            else:
                print(("{0}, you won!").format(player2_name))
            return True

    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != "_":
        if board[1][1] == "O": 
            print(("{0}, you won!").format(player1_name))
            return True
        else:
            print(("{0}, you won!").format(player2_name))
            return True
    if board[2][0] == board[1][1] == board[0][2] and board[1][1] != "_":
        if board[1][1] == "O": 
            print(("{0}, you won!").format(player1_name))
            return True
        else:
            print(("{0}, you won!").format(player2_name))
            return True

    # Vertical
    if (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
        #global victory = True
        if board[0][0] == "O" or board[0][1] == "O" or board[0][2] == "O": 
            print(("{0}, you won!").format(player1_name))
        else:
            print(("{0}, you won!").format(player2_name))
    if (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
        #global victory = True
        if board[0][0] == "X" or board[0][1] == "X" or board[0][2] == "X": 
            print(("{0}, you won!").format(player1_name))
        else:
            print(("{0}, you won!").format(player2_name))
        return True

    return False

### MAIN ###

f = Figlet(font='slant')           
print(f.renderText('O & X'))

play = True
name1 = (str(input("Player1, what's your name? "))).upper()
name2 = (str(input("Player2, what's your name? "))).upper()
print("Hello " + name1 + " and " + name2 + "! Let's play!")

player1_name, player2_name = select_random_player()
player1_sign, player2_sign = sign_assignment()
if player1_sign == "O":
    players = ['O', 'X']
else:
    players = ['X', 'O']

while play:

    board = [
        ["_", "_", "_",],
        ["_", "_", "_",],
        ["_", "_", "_",],
        ]
    game_won = False
    board, _ = display_board(board, just_display=True)
    player_choice = cycle(players)
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")             
        played = True

        while played:
            while True:
                try:
                    row = int(input("Please enter the row number (0, 1, 2): "))
                    if row == 0 or row == 1 or row ==2:
                        break
                    else:
                       print("The only valid inputs are 0, 1 or 2!") 
                except ValueError:
                    print("Are you looking for a job as a tester in TicTacToc & Co.?")
                except IndexError:
                    print("The only valid inputs are 0, 1 or 2!")
                except TypeError:
                    print("Are you looking for a job as a tester in TicTacToc & Co.?")
            while True:
                try:
                    column = int(input("Please enter the column number (0, 1, 2): "))
                    if row == 0 or row == 1 or row ==2:
                        break
                    else:
                       print("The only valid inputs are 0, 1 or 2!") 
                except ValueError:
                    print("Are you looking for a job as a tester in TicTacToc & Co.?")
                except IndexError:
                    print("The only valid inputs are 0, 1 or 2!")
                except TypeError:
                    print("Are you looking for a job as a tester in TicTacToc & Co.?")
            if board[row][column] != "_":
                print("It's occupied. Choose another one!")
            else:
                board, played = display_board(board, current_player, row, column)
                board[row][column] = current_player
                played = False

        if win(board):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n)?")
            if again.lower() == "y":
                print("Initiating the game.")
            elif again.lower() == "n":
                print("Bye!")
                play = False
            else:
                print("Not the correct input. Closing the game.")
                play = False
