# import the random module
import random

# create a list of three options rock, paper, or scissors
options = ["rock", "paper", "scissors"]

# create a variable to store the number of wins and rounds
wins = 0
rounds = 0

# create a while loop that will run until the user decides to quit
while True:

    # ask the user to input their choice
    user_choice = input("Enter rock, paper, or scissors: ")

    # convert the user's choice to lowercase
    user_choice = user_choice.lower()

    # check if the user's choice is valid
    if user_choice not in options:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    # randomly select the computer's choice
    computer_choice = random.choice(options)

    # print the computer's choice
    print(f"Computer chose: {computer_choice}")

    # check if the user's choice is equal to the computer's choice
    if user_choice == computer_choice:
        print("It's a tie!")
    # check if the user's choice is rock and the computer's choice is scissors
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        wins += 1
    # check if the user's choice is paper and the computer's choice is rock
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        wins += 1
    # check if the user's choice is scissors and the computer's choice is paper
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        wins += 1
    # if none of the above conditions are met, the computer wins
    else:
        print("Computer wins!")

    # increment the number of rounds
    rounds += 1

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

    # convert the user's choice to lowercase
    play_again = play_again.lower()

    # check if the user's choice is invalid
    if play_again not in ["yes", "no"]:
        print("Invalid choice. Please enter yes or no.")
        continue    

    # if the user does not want to play again, break out of the loop
    if play_again == "no":
        break

# print the number of wins and rounds
print(f"Number of wins: {wins}")
print(f"Number of rounds: {rounds}")