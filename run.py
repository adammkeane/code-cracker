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

        intro_choice = input("Enter your selection here: ")
        
        
        if validate_data(intro_choice):
            print("What a fine choice.")
            break

    return intro_choice       

def main():
    get_intro_choice()

logo = Figlet(font="5lineoblique")
print(logo.renderText("Code Cracker"))
print("Crack the code and win 1 million dollars.")
print("(actual cash prize may be sigificantly less than that)\n")

main()