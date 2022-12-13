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