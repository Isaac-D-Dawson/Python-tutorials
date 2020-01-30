#Rock Paper Scissors
#Version 1:
#   Asks two users for input
#   Compares input
#   Returns winner

player0 = input("Player One enter your choice: ").lower()
player1 = input("Player Two enter your choice: ").lower()

if player0 == "rock" and player1 == "paper" or player0 == "paper" and player1 == "scissors" or player0 == "scisors" and player1 == "rock" :
    winner = "Player Two"
else:
    winner = "player One"

if player0 == player1:
    print("It's a Tie! No winners here, but no losers either.")
else:
    print(f"{winner} Wins!")

# if #Either player picked something other than rock, paper, or scisors
#     print("Hey, what're you tryna pull here! Rock, Paper, or Scissors only you two!")
#     print(" *Sigh*. End users... Nutters the lot of them. *Grumble Grumble*")
# else:
#     print(f"{winner} Wins!")