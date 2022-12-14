import random
import art

# Beginning of the game.
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

# Print the art of the user choice.
if user_choice == "Rock":
    print(art.rock)
elif user_choice == "Paper":
    print(art.paper)
else:
    print(art.scissors)

# Print the art of the computer choice.
if computer_choice == "Rock":
    print(f"Computer chose:\n{art.rock}")
elif computer_choice == "Paper":
    print(f"Computer chose:\n{art.paper}")
else:
    print(f"Computer chose:\n{art.scissors}")

# Determine the winner.
if user_choice == computer_choice:
    print("It's a draw!!")
elif user_choice == "Rock":
    if computer_choice == "Scissors":
        print("You win!!!")
    else:
        print("You lose!")
elif user_choice == "Paper":
    if computer_choice == "Rock":
        print("You win!!!")
    else:
        print("You lose!")
elif user_choice == "Scissors":
    if computer_choice == "Paper":
        print("You win!!!")
    else:
        print("You lose!")