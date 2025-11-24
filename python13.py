import random

print("🎲 Simple Dice Roller 🎲")

while True:
    input("Press Enter to roll the dice...")
    roll = random.randint(1, 6)
    print(f"You rolled: {roll}")
    
    again = input("Roll again? (y/n): ").lower()
    if again != "y":
        print("Goodbye! 👋")
        break
