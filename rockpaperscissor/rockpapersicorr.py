import random

def game():
    player = input("Enter Rock(r), Paper(p) or Scissor(s) :")
    opponent = random.choice(['r', 'p', 's'])
    print(f"User's Choice: {player}")
    print(f"Computer's Choice: {opponent}")
    if player == opponent:
        print("It's a tie!")
    elif player == 'p' and opponent == 's' or player == 'r' and opponent == 'p' or player == 's' and opponent == 'r':
        print("Oops! Computer won, Better luck next time")
    else:
        print("Yayy! Congratulations you won!")

game()