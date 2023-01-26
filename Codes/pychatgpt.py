import openai, json

with open ("config.json") as f:
    config = json.load(f)

openai.api_key = config['api_key']

def chatbot():
    # Initialize conversation context
    conversation_context = ""

    while True:
        # Ask user for input
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            # Use the conversation context and user input as the prompt
            prompt = conversation_context + user_input
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n =1,
                stop=None,
                temperature = 0.5
            )
            # Save the response text as the new conversation context
            conversation_context = response["choices"][0]["text"]
            # Print the response
            print(f"Chatbot: {conversation_context}\n")

chatbot()

