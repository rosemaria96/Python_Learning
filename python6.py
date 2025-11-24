# Simple Quiz Game in Python

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. Java", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["A. J.K. Rowling", "B. Tolkien", "C. Agatha Christie", "D. Dan Brown"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    }
]

score = 0

print("\n Welcome to the Python Quiz Game!\n")
username = input("Enter your name: ")
print(f"\nHello, {username}! Let's start the quiz.\n")

for index, q in enumerate(questions):
    print(f"Q{index + 1}: {q['question']}")
    for option in q['options']:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q['answer']:
        print(" Correct!\n")
        score += 1
    else:
        print(f" Wrong! The correct answer was {q['answer']}.\n")

print(" Quiz Completed!")
print(f"{username}, your final score is: {score}/{len(questions)}")

if score == len(questions):
    print(" Excellent! You're a quiz master!")
elif score >= 3:
    print(" Good job! Keep practicing.")
else:
    print(" Keep learning and try again!")

