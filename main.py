import random

# Begining of the game.
# Instead of let the user write "rock", "paper" or "scissors" I choose
# represent each one with the numbers "0", "1" and "2", that way I believe
# that is easier for the user and also lowers the chance of they making a
# mistake while writing.
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

# Randomly select the computer option.
possibilities = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(possibilities)

# Switched the values for better code readability.
if user_choice == "0":
    user_choice = "Rock"
elif user_choice == "1":
    user_choice = "Paper"
elif user_choice == "2":
    user_choice = "Scissors"
else:
    print("The chosen option isn't valid.")