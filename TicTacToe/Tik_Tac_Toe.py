
import random
current_player = {"current_player": "X"}
magic_square = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]


#Chooses randomly who starts
def choose_starter_mark():
    if random.randint(0,1) == 0:
        return "X"
    else:
        return "O"


# Check if current_player has won the board.
# Returns True if won, False otherwise
def check_winner(board, current_player_mark):
    is_winner = False
    magic_square_calc_diag = 0
    magic_square_calc_anti_diag = 0

    # Checks if current_player has won the diagonal or reverse diagonal
    for diag in range(3):
        if board[diag][diag] == current_player_mark:
            magic_square_calc_diag += magic_square[diag][diag]
        if board[2-diag][diag] == current_player_mark:
            magic_square_calc_anti_diag += magic_square[2-diag][diag]
        if magic_square_calc_diag == 15 or magic_square_calc_anti_diag == 15:
            is_winner = True

    magic_square_calc = 0
    # Checks if winner is in single row or single column
    for row in range(3):
        for col in range(3):
            if board[row][col] == current_player_mark:
                magic_square_calc += magic_square[row][col]
            if magic_square_calc == 15:
                is_winner = True

    return is_winner


#Dispays game matrix
def display(matrix):
    print("Tic tac toe")
    print("\n")
    print("Rad 0 " + str(matrix[0]))
    print("Rad 1 " + str(matrix[1]))
    print("Rad 2 " + str(matrix[2]))


#Checks user input for row choice
def user_input_row():
    acceptable_range = ['0', '1', '2']
    user_choice = "START"
    while user_choice not in acceptable_range:
        user_choice = input("Välj rad 0-2: ")
        if user_choice not in acceptable_range:
            print("Värde ej inom scope, välj 0-2")
    return user_choice


#Checks user input for col choice
def user_input_col():
    acceptable_range = ['0', '1', '2']
    user_choice = "START"
    while user_choice not in acceptable_range:
        user_choice = input("Välj kolumn 0-2: ")
        if user_choice not in acceptable_range:
            print("Värde ej inom scope, välj 0-2")
    return user_choice


#Main method for Tic tac toe game
if __name__ == '__main__':
    tic_tac_toe = [[None for col in range(3)]for row in range(3)]
    game_close = "N"
    current_player["current_player"] = choose_starter_mark()
    while game_close != "Y":
        print('\n'*100)
        display(tic_tac_toe)
        print(f'Välj ruta för {current_player["current_player"]}')
        row_number = int(user_input_row())
        col_number = int(user_input_col())
        if tic_tac_toe[row_number][col_number] is not None:
            print("Ruta upptagen, välj annan")
            continue
        else:
            tic_tac_toe[row_number][col_number] = current_player["current_player"]
            if check_winner(tic_tac_toe, current_player["current_player"]):
                print('\n' * 100)
                display(tic_tac_toe)
                print(str(current_player["current_player"]) + str(" har vunnit!"))
                game_close = "Y"
                break
            # Checks for None, since we start with board full of None
            space_exists = any(None in sub for sub in tic_tac_toe)
            if not space_exists:
                print("Speltavla full")
                break
            if current_player["current_player"] == "X":
                current_player["current_player"] = "O"
            else:
                current_player["current_player"] = "X"
        game_close = input("Vill du avsluta, Y?: ")
    print("Spel avslutat")