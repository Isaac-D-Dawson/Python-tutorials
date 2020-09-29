#Rock Paper scissors

print("importing pre-requisites...")
#Grab random so we can use choice
import random as rand

#Patch notes:
#Ver 1.0:
#-Game created
#Ver 2.0:
#-Draw conditions added.
#Ver 3.0:
# Options for Human v Computer play installed
#ver 4.0:
# Enabled repeat play.
#ver 5.0:
# allowed for cheat detection. no more crashes by entering a null value!

print("creating environment variables")
#valid choices
valid = ("rock", "paper", "scissors")

#set up while variable
repeat = 0

#options for how the computer will play
#   Leaving as list no tuple for now for future expansion
#              '''[Computer enabled, Play Mode]'''
compOptions = [False, 1]
#Modes:
# 0: Pick a choice at random
# 1: Pick a choice at random, weighted to tie

print("Rock-Paper-Scissors module installed! PLease enjoy")

#start while loop
while repeat == 0:
    if compOptions[0] == False:
        print("Player One please pick your option")
        player1 = input().lower()
        print("Player Two please pick your option")
        player2 = input().lower()
    else:
       print("Human Player, please make your choice")
       player1 = input().lower()

    # print(valid.index(player1))

    #Generate weights for compPlay
    if compOptions[0] == True and compOptions[1] != 0:
        weight = [1, 1, 1]
        weight[(valid.index(player1))] =+ 3

        #Computer makes choice
        if compOptions[1] == 0:
            player2 = rand.choice(valid)
        if compOptions[1] == 1:
            player2 = rand.choices(valid, weights= weight, k=1)[0]
        # if compOptions[1] == 2:
        #     player2 = rand.choices(valid, weights= weight, k=1)
    

    #compare results

    #player one wins
    #paper beats rock beats scisors beats paper
    if player1 == "paper" and player2 == "rock" or player1 == "rock" and player2 == "scissors" or player1 == "scissors" and player2 == "paper":
        winner = "One"
    #player two wins
    if player2 == "paper" and player1 == "rock" or player2 == "rock" and player1 == "scissors" or player2 == "scissors" and player1 == "paper":
       winner = "Two"

    #Tie
    if player1 == player2:
        winner = "Tie"

    #cheat!
    if player1 not in valid or player2 not in valid:
        winner = "No Win"

    winCondition = {"One":"Player One Wins!", "Two":"Player Two Wins!", "Tie":"Tie! No winners, but no losers!", "No Win":"Hey, One of you cheated! No winning for either of you!"}

    #Commented out to fix the draw condition.
    # print(f"the winner is Player {winner}")

    print(winCondition[winner])
    print("Would you like another game?(y/n)")
    if input().lower() == "n":
        repeat = 1
print("Thanks for playing! :)")
print("We hope to see you again!")