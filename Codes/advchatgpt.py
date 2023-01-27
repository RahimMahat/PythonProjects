import openai
import spacy
from transformers import pipeline

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")

# Initialize sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Initialize the context
context = ""

openai.api_key = "YOUR_API_KEY"
model_engine = "text-davinci-002"

# Function to extract entities from user input using spaCy
def extract_entities(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        entities[ent.label_] = ent.text
    return entities

# Function to generate response from GPT-3
def generate_response(prompt, previous_context, entities):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        context=previous_context,
        entities=entities
    )
    return completions.choices[0].text

# Dialogue management function
def manage_dialogue(user_input, context):
    entities = extract_entities(user_input)
    sentiment = sentiment_pipeline(user_input)[0]["label"]
    bot_response = generate_response(user_input, context, entities)
    # Add actions based on sentiment and entities
    if sentiment == "NEGATIVE":
        bot_response = "I'm sorry to hear that. How can I help you?"
    if "location" in entities:
        bot_response += f" Do you have any plans to visit {entities['location']}?"
    return bot_response

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    bot_response = manage_dialogue(user_input, context)
    print("Bot: ", bot_response)
    context = f"{context} {user_input} {bot_response}"

