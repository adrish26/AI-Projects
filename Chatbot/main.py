import random

# Define responses for different user inputs
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I assist you with?",
    "how are you": "I'm just a chatbot, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "what's your name": "I'm just a chatbot, so I don't have a name.",
    "weather": "I'm sorry, I can't provide weather information at the moment.",
    "joke": "Why don't scientists trust atoms? Because they make up everything!",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?",
}

# Function to handle user input and provide responses
def chatbot():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print(responses["bye"])
            break
        response = responses.get(user_input, responses["default"])
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()