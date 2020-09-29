#Rock Paper scissors

#Patch notes:
#Ver 1.0:
#-Game created
#Ver 2.0:
#-Draw conditions added.

#valid choices
#valid = ["rock", "paper", "scissors"]

print("Player One please pick your option")
player1 = input().lower()
print("Player Two please pick your option")
player2 = input().lower()

# print(valid.index(player1))

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

winCondition = {"One":"Player One Wins!", "Two":"Player Two Wins!", "Tie":"Tie! No winners, but no losers!", "No Win":"Hey, One of you cheated! No winning for either of you!"}

#Commented out to fix the draw condition.
# print(f"the winner is Player {winner}")

print(winCondition[winner])