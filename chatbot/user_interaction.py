# user_interaction.py

def get_user_input(prompt):
    """Function to get input from the user."""
    return input(prompt)

def display_message(message):
    """Function to display a message to the user."""
    print(message)

def welcome_user():
    """Function to welcome the user."""
    display_message("Welcome to the Chatbot! How can I assist you today?")

def handle_user_query(query):
    """Function to handle user queries."""
    # Here you would typically call your NLP model or processing function
    # For demonstration, we'll just echo the input
    response = f"You said: {query}"
    return response

def main():
    """Main function to run the chatbot interaction."""
    welcome_user()
    
    while True:
        user_input = get_user_input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            display_message("Goodbye! Have a great day!")
            break
        
        response = handle_user_query(user_input)
        display_message(f"Chatbot: {response}")

if __name__ == "__main__":
    main()