print("Welcome to the Rock-Paper-Scissors Game!")

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Get the player 1's choice
player1 = input("Player 1, choose rock, paper, or scissors: ").lower()
while player1 not in choices:
    print("Invalid choice, try again.")
    player1 = input("Player 1, choose rock, paper, or scissors: ").lower()

# Get the player 2's choice
player2 = input("Player 2, choose rock, paper, or scissors: ").lower()
while player2 not in choices:
    print("Invalid choice, try again.")
    player2 = input("Player 2, choose rock, paper, or scissors: ").lower()

# Determine the winner
if player1 == player2:
    print("It's a tie!")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 wins with rock!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins with paper!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins with scissors!")
else:
    print("Player 2 wins!")
