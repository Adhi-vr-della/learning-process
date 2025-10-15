import random

secrete = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess: "))
    if guess > secrete:
        print("Your guess is too high.")
    elif guess < secrete:
        print("Your guess is too low.")
    else:
        print("You guessed the secret number.")
        break