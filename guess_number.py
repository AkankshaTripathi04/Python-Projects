import random

def guess(x):
    random_number = random.randint(1,x)
    guess_number = 0
    print(f"guess a number between 1 and {x}")
    while guess_number != random_number:
        guess_number = int(input("guess the number: "))
        if (guess_number < random_number):
            print("Try a little higher")
        elif (guess_number > random_number):
            print("Try a little lower")
    print(f"Congrats! You guessed {random_number} correctly!")

def comp_guess(x):
    feedback = ""
    low = 1
    high = x

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} correct , lower or higher than the needed number?: ")
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    print(f"The number is {guess}")

comp_guess(5)