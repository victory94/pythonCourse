current_player = {"current_player": "X"}


def display(matrix):
    print("Tic tac toe")
    print("\n")
    print("Rad 1 " + str(matrix[0]))
    print("Rad 2 " + str(matrix[1]))
    print("Rad 3 " + str(matrix[2]))


def user_input_row():
    acceptable_range = ['0', '1', '2']
    user_choice = "START"
    while user_choice not in acceptable_range:
        user_choice = input("Välj rad 0-2: ")
        if user_choice not in acceptable_range:
            print("Värde ej inom scope, välj 0-2")
    return user_choice


def user_input_col():
    acceptable_range = ['0', '1', '2']
    user_choice = "START"
    while user_choice not in acceptable_range:
        user_choice = input("Välj kolumn 0-2: ")
        if user_choice not in acceptable_range:
            print("Värde ej inom scope, välj 0-2")
    return user_choice


if __name__ == '__main__':
    tic_tac_toe = [["-" for col in range(3)]for row in range(3)]
    game_close = "N"
    while game_close != "Y":
        display(tic_tac_toe)
        # TODO: Add logic to check if someone won.
        print(f'Välj ruta för {current_player["current_player"]}')
        row_number = int(user_input_row())
        col_number = int(user_input_col())
        if tic_tac_toe[row_number][col_number] != "-":
            print("Ruta upptagen, välj annan")
            continue
        else:
            tic_tac_toe[row_number][col_number] = current_player["current_player"]
            if current_player["current_player"] == "X":
                current_player["current_player"] = "O"
            else:
                current_player["current_player"] = "X"
        game_close = input("Vill du avsluta, Y?: ")