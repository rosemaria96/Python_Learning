import random

print("Welcome to the Dice Rolling Simulator!")

while True:
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}")

    play_again = input("Roll again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
