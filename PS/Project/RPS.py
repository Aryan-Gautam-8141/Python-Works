import random

# Function to determine the winner
def RPS():
    dict = {1: "Rock", 2: "Paper", 3: "Scissors"}    # Assigning values to choices means input 1 and display Rock etc.
    print(f"User chose: {dict[user]} \nComputer chose: {dict[computer]}")
    print("---Result---")
    if user == computer:
        print("It's a tie!")
    elif (user == 1 and computer == 3) or \
        (user == 2 and computer == 1) or \
        (user == 3 and computer == 2):
        print("You win!")
    else:
        print("Computer wins!")

print('''Rock = 1
Paper = 2
Scissors = 3''')

user = int(input("Enter your choice : "))
computer = random.randint(1, 3)

# Input validation Else call RPS function
if user > 3 or user < 1:
    print("Invalid input!")
else:
    RPS()