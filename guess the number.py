import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 4 and {x}:"))
        if guess < random_number:
            print(f"Sorry, Guess again your number {x} is too low")
        elif guess > random_number:
            print (f"Sorry, Guess again, Your number{x} is too high")
    print (f"Yay!!!, congrats, You have guessed the right number {random_number}")
    
    
    
guess(15)