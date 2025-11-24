import random

# Predefined responses
responses = {
    "hi": ["Hello!", "Hey there!", "Hi, how can I help you?"],
    "how are you": ["I'm doing great!", "Feeling awesome!", "All good, thanks!"],
    "bye": ["Goodbye!", "See you later!", "Bye, have a nice day!"],
    "default": ["I'm not sure I understand.", "Could you say that again?", "Interesting! Tell me more."]
}

def ai_agent(user_input):
    # Normalize input
    user_input = user_input.lower()

    # Check if user_input matches known patterns
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# Run chatbot
print("AI Agent: Hi, I’m your simple AI assistant. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("🤖 AI Agent:", random.choice(responses["bye"]))
        break
    response = ai_agent(user_input)
    print("🤖 AI Agent:", response)
