import openai

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'

def generate_response(message):
    # Generate a response using ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Extract the generated response
    generated_text = response.choices[0].text.strip()
    
    return generated_text

# Main loop for the chatbot
while True:
    user_input = input("User: ")
    
    # Exit the loop if the user enters 'exit'
    if user_input.lower() == 'exit':
        break
    
    # Generate a response using the user input
    bot_response = generate_response(user_input)
    
    print("Chatbot:", bot_response)
