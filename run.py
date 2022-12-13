from random import randint


def make_sea():
    """
    Function to take in user input and create playing grid
    """
    sea = []
    valid_size = False
    while valid_size == False:
        try:
            sea_size = int(
                input("\nHow large would you like the sea? (2 - 8):")
            )
            if (sea_size < 2):
                print("Sea too small, please enter again.")
            elif (sea_size > 10):
                print("Sea too large, please enter again")
            else:
                for _ in range(sea_size):
                    sea.append([0] *sea_size)
                valid_size = True
        except ValueError:
            print("Not an integer, please try agian.")
    return sea

def player_ship_location(sea):
    """
    Function for player to enter in where they want their ship to be placed.
    """
    valid_ship_row = False
    Valid_ship_col = False
    Print("Enter ship coordinates.\nPlease enter between 1 - {}".format(len(sea)))
    while valid_ship_row == False:
        try:
            player_ship_row = int(
                input("Enter row where you want your ship:")
            )
            if (player_ship_row not in range(1, len(sea) + 1)):
                print("Not valid coordinates,please enter a number between 1 - {}".format(len(sea) + 1))
            else:
                valid_ship_row = True
        except ValueError:
            print("Not an integer,please try again.")
    while valid_ship_col == False:
        try:
            player_ship_col = int(
                input("Enter column where you want your ship: "))
            print(" ")
            if (player_ship_col not in range(1, len(sea) + 1)):
                print(
                    "Not valid column coordinates, please enter a number between 1 - {}".format(len(sea) + 1))
            else:
                sea[player_ship_row - 1][player_ship_col - 1] = "#"
                valid_ship_col = True
        except ValueError:
            print("Not an integer, please try again")

    return sea


def random_row(sea):
    return randint(0, len(sea) - 1)


def random_col(sea):
    return randint(0, len(sea[0]) - 1)


def find_enemy_ship(sea):
    valid_enemy_ship_location = False
    while(valid_enemy_ship_location == False):
        enemy_ship_row = random_row(sea)
        enemy_ship_col = random_col(sea)
        # Prevents computer to choose your ship coordiantes
        if (sea[enemy_ship_row][enemy_ship_col] != "#"):
            valid_enemy_ship_location = True
    return enemy_ship_row, enemy_ship_col


def print_sea(sea):
    """
    Function to print the board.
    """
    for row in sea:
        print(("   ").join(row))
    print(" ")


def row_guess(sea):
    """
    Function for player to choose a row where he wants to hit.
    """
    valid_row = False
    print(("Enter attack coordinates.\nPlease enter number from 1 - {}").format(len(sea)))
    while (valid_row == False):
        try:
            guess_row = int(input("Guess Row"))
            if (guess_row not in range(1, len(sea) + 1)):
                print(("Not a valid row, please enter from 1 - {}").format(len(sea)))
            else:
                valid_row = True
        except ValueError:
            print("Not an integer, plaese try again.")
    
    return guess_row - 1


def col_guess(sea):
    """
    Function for palyer to choose a column where he wants to hit.
    """
    valid_col = False
    while(valid_col == False):
        try:
            guess_col = int(input("Guess Column: "))
            if (guess_col not in range(1, len(sea)+1)):
                print(
                    ("Not a valid row, please enter number from 1 - {}: ").format(len(sea)))
            else:
                valid_col = True
        except ValueError:
            print("Not an integer, please try again")
    
    return guess_col - 1


def enemy_turn(sea, enemy_guess_count, enemy_ship_row, enemy_ship_col):
    """
    Function that has the logic for the computer to choose random valid coordinates to attack.
    """
    valid_enemy_attack = False
    while (valid_enemy_attack == False):
        attack_row = random_row(sea)
        attack_col = random_col(sea)
        # Enemy hit your ship
        if (sea[attack_row][attack_col] == "#"):
            print("\nEnemy sunk your battleship! You lose!")
            print("The enemy sunk your battleship in {} tries\n".format(enemy_guess_count))
            valid_enemy_attack = True
            return True
        # Prevents AI from choosing already entered coordinate
        elif (sea[attack_row][attack_col] != "O"):
            continue
        # Prevents AI from choosing their ships coordinates
        elif (attack_row == enemy_ship_row and attack_col == enemy_ship_col):
            continue
        # Prints the enemy attack if missed
        else:
            sea[attack_row][attack_col] = "*"
            print("ENEMY MOVE")
            print_sea(sea)
            valid_enemy_attack = True
    return False


def player_turn(sea, valid_guess_count, enemy_ship_row, enemy_ship_col):
    """
    Function for the player to choose coordintes where player wants to attack.
    """
    valid_player_turn = False
    while (valid_player_turn == False):
        guess_row = row_guess(sea)
        guess_col = col_guess(sea)

        # Already played coordinates
        if (sea[guess_row][guess_col] == "X" or sea[guess_row][guess_col] == "*"):
            print("Coordinates already entered, Try again")
        # Player entered their ship coordinates
        elif (sea[guess_row][guess_col] == "#"):
            print("Don't blow yourself up now... Try again")
        # Prints the player attack if missed
        elif (guess_row != enemy_ship_row or guess_col != enemy_ship_col):
            sea[guess_row][guess_col] = "X"
            print("\nPLAYER MOVE")
            print_sea(sea)
            print("You missed the battleship!\n")
            valid_player_turn = True
        # player hit enemy ship
        else:
            print("\nYou sunk the battleship! You win!")
            print(
                "It took {} valid tries to win\n".format(valid_guess_count))
            return True
    
    return False