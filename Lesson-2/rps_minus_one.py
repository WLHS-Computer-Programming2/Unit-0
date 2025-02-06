"""
Name: Mr. Smith
File: rps_minus_one.py
Description: Implements the Rock Paper Scissor Minus One
game from Squid Game
"""

"""
Pseudocode
Have computer pick two random "hands" of rps
SET comp_score, player_score to 0
STORE values in comp_hand somehow (you choose)
ASK user for their hands
STORE values in player_hand
ASK user which hand to keep
computer randomly chooses hand
EVALUATE who wins
UPDATE score
ASK if they want to continue or quit
IF quit, PRINT scores and END game
    ELSE play again
"""
import random

def comp_choice(options):
    comp_choice1 = random.randint(0,2)
    comp_choice2 = random.randint(0,2)
    comp_hands = (options[comp_choice1],options[comp_choice2])
    return comp_hands

def determine_winner(hand1,hand2,scores):
    if hand1 == hand2:
        return "The result is a tie"
    elif (hand1 == "rock" and hand2 == "scissors") or (hand1 == "paper" and hand2 == "rock") or (hand1 == "scissors" and hand2 == "paper"):
        scores[0] += 1
        return "The player wins this round"
    else:
        scores[1] += 1
        return "The computer wins this round"

def print_score(scores):
    print(f"The player has a score of {scores[0]} and the computer has a score of {scores[1]}")

def player_hands(options):
    scores = [0,0] # first is player, second is computer
    player_hand1 = int(input("Left hand: Please choose rock(1), paper(2), or scissors(3) "))
    player_hand2 = int(input("Right hand: Please rock(1), paper(2), or scissors(3) "))
    player_hands = (options[player_hand1-1],options[player_hand2-1])
    return player_hands

def main():
    scores = [0,0]
    options = ["rock","paper","scissors"]
    comp = comp_choice(options)
    player = player_hands(options)
    
    print(f"The computer has chosen: {comp[0]} and {comp[1]}")
    print(f"You have chosen: {player[0]} and {player[1]}.")

    print(determine_winner(player,comp,scores))
    print_score(scores)
    
main()