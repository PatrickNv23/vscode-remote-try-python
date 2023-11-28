#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

#write 'hello world' to the console
#print("hello world")

player_points = 0
computer_points = 0
attempts = 0

def play_rock_paper_scissors(player, computer):
    options = ["rock", "paper", "scissors"]

    if player == computer:
        return "It's a tie!"

    if player == "rock":
        if computer == "paper":
            return "Computer wins"
        else:
            return "Player wins"

    if player == "paper":
        if computer == "scissors":
            return "Computer wins"
        else:
            return "Player wins"

    if player == "scissors":
        if computer == "rock":
            return "Computer wins"
        else:
            return "Player wins"
        
#Create a function to ask the user if they want to play again
def play_again():
    global attempts
    attempts = attempts + 1

    play_again = input("Do you want to play again? (y/n) -> ").lower()
    if play_again == "y":
        main()
    else:
        print("Thanks for playing!")
        final_points()

#Create a function to store the points of the player and computer in total until they decide to stop playing
def points(result):
    global player_points
    global computer_points

    if result == "It's a tie!":
        player_points = player_points + 1
        computer_points = computer_points + 1
    if result == "Computer wins":
        computer_points = computer_points + 1
    if result == "Player wins":
        player_points = player_points + 1
    return player_points, computer_points


#Create a function to show the points of the player and computer in total when the game is over
def final_points():
    global player_points
    global computer_points
    global attempts

    print(f"Player points: {player_points}")
    print(f"Computer points: {computer_points}")
    print(f"Number of attempts: {attempts}")

#Create a function to validate the input of the user (convert to lowercase and check if it is a valid option)
def validate_input():
    player = input("Select an option: rock, paper, scissors -> ").lower()
    while player != "rock" and player != "paper" and player != "scissors":
        print("Invalid option. Please try again.")
        player = input("Select an option: rock, paper, scissors -> ").lower()
    return player


def main():
    player = validate_input()
    computer = random.choice(["rock", "paper", "scissors"])
    result = play_rock_paper_scissors(player, computer)
    print(f"Player selected {player}")
    print(f"Computer selected {computer}")
    print(result)
    points(result)
    play_again()

if __name__ == '__main__':
    print("Welcome to the Rock_Paper_Scissors game!")
    main()

