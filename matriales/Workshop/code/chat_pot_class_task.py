import random
from responses import responses  # Import responses from the external file

# Function to get a response based on user input
def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

# Chatbot class
class Chatbot:
    def chat(self):
        """Start the chatbot conversation."""
        print("Chatbot: Hi! How can I assist you today?")
        
        while True:
            user_input = input("User: ").lower()
            response = get_response(user_input)
            print("Chatbot:", response)
            
            if user_input == "goodbye":
                break

# Instantiate and run the chatbot
chatbot = Chatbot()
chatbot.chat()
