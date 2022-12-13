from random import randint


def make_sea():
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
