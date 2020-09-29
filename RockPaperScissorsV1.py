#Rock Paper scissors

print("Player One please pick your option")
player1 = input().lower()
print("Player Two please pick your option")
player2 = input().lower()

#compare results

#player one wins
#paper beats rock beats scisors beats paper
if player1 == "paper" and player2 == "rock" or player1 == "rock" and player2 == "scissors" or player1 == "scissors" and player2 == "paper":
    winner = "One"
#player two wins
if player2 == "paper" and player1 == "rock" or player2 == "rock" and player1 == "scissors" or player2 == "scissors" and player1 == "paper":
    winner = "Two"

print(f"the winner is Player {winner}")