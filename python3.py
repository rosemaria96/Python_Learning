#PASSWORD GENERATOR

import random
import string

def generate_password(length, uppercase, lowercase, numbers, symbols):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Error, no characters found")
        return None
    
    password = "".join(random.choice(characters) for _ in range(length)) 
    return password

length = int(input("Enter the password length: "))
uppercase = input("Include Uppercase? (yes/no): ").strip().lower() == "yes"
lowercase = input("Include Lowercase? (yes/no): ").strip().lower() == "yes"
numbers = input("Include Numbers? (yes/no): ").strip().lower() == "yes"
symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

password = generate_password(length, uppercase, lowercase, numbers, symbols)

if password:
    print("Generate Password:", password)
