import random
from time import sleep


print("\n\nYou are playing the game of \"Guess the number\"!")
sleep(2)

while True:

    print("\nGuess a number between 1 and 50, you have 5 attempts!")
    number_of_guesses = 0
    pc = random.randint(1, 50)

    while number_of_guesses < 5:
        guess = int(input("> "))
        number_of_guesses += 1
        guesses_left = 5 - number_of_guesses
        if guess < pc:
            print(f"The number is HIGHER ({guesses_left} attempts left)")
        if guess > pc:
            print(f"The number is LOWER ({guesses_left} attempts left)")
        if guess == pc:
            break

    if guess == pc:
        print(f"\nYOU GOT IT - in {number_of_guesses} attempts!")
    else:
        print(f"\nYOU LOST! The number was {pc}")

    play_again = str(input("\nPlay again? (y/n): "))
    if play_again.lower() != "y":
        break
