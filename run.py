# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# python3 run.py

# import pyfiglet
from pyfiglet import Figlet


def get_intro_choice():
    """
    Get intro selection from user: whether they want to play the game, or see how to play first
    """
    while True:
        print("1 : Play Game")
        print("2 : How to Play\n")
        print("Type '1' or '2' for the option you want to select, and then press Enter please.")

        initial_input = input("Enter your selection here: ")

        # In case user literally types something like '1', instead of 1
        intro_choice = initial_input.replace("'", "")
     
        if validate_data(intro_choice):
            print("\nWhat a fine choice.\n")
            break

    return intro_choice       


def validate_data(choice):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        choice = int(choice)
        if choice != 1 and choice != 2:
            raise ValueError(
                f"\nOnly '1' or '2' required. You provided {choice}"
            )
    except ValueError as e:
        print("\n---------------------")
        print(f"\nInvalid data: {e}. Please try again.\n")
        print("---------------------\n")
        return False

    return True


def main():
    get_intro_choice()

logo = Figlet(font="5lineoblique")
print(logo.renderText("Code Cracker"))
print("Crack the code and win 1 million dollars.")
print("(actual cash prize may be sigificantly less than that)\n")

main()