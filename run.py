# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# python3 run.py

import random
# import pyfiglet
from pyfiglet import Figlet


def get_intro_choice():
    """
    Get intro selection from user: 
    whether they want to play the game, or see how to play first
    """
    while True:
        print("1 : Play Game")
        print("2 : How to Play\n")
        print("Type '1' or '2' for the option you want to select, and then press Enter please.\n")

        initial_input = input("Enter your selection here: ")

        # In case user literally types something like '1', instead of 1
        intro_choice = initial_input.replace("'", "")
     
        if validate_data(intro_choice):
            print("\nWhat a fine choice.\n")
            break

    return int(intro_choice)       


def validate_data(choice):
    """
    Inside the try, converts string value into integer.
    Raises ValueError if strings cannot be converted into int,
    or if they pick an integer that's.
    """
    try:
        choice = int(choice)
        if choice != 1 and choice != 2:
            raise ValueError(
                f"\nOnly '1' or '2' required. You provided {choice}"
            )
    except ValueError as e:
        print("\n-------------------------------------")
        print(f"\nInvalid data: {e}. Please try again.\n")
        print("-------------------------------------\n")
        return False

    return True


def how_to_play():
    """
    Show user instructions how to play the game
    """
    print("-----------")
    print("HOW TO PLAY") 
    print("-----------\n")
    print("At the start of each game, a secret 4 digit code with be generated.")
    print("You'll have 5 attempts to figure out the code.\n")
    print("For each attempt, enter a 4 digit code.")
    print("After each attempt, we'll let you know how close you were to cracking the code.\n")
    print("To do this, we'll reprint your 4 digit attempt, adding colors to each digit.\n")
    print("Red: this digit is not in the secret code.")
    print("Yellow: this digit is in the secret code, but is not in the correct postion.")
    print("Green: this digit is in the secret code, and is in the correct postion!\n")
    print("------------------------------------------")
    print("NOW THAT YOU KNOW THE RULES, LET'S PLAY :)") 
    print("------------------------------------------\n")


def generate_code():
    """
    Generates a random list of 4 digits for our secret game code
    """
    code = random.sample(range(1,10),4)
    return code


def main():
    """.
    Runs all functions of the game
    """
    intro_choice = get_intro_choice()  
    if intro_choice == 1:
        how_to_play()
    code = generate_code()
    print(code) 

        
logo = Figlet(font="5lineoblique")
print(logo.renderText("Code Cracker"))
print("Crack the code and win 1 million dollars.")
print("(actual cash prize may be sigificantly less than that)\n")

main()
