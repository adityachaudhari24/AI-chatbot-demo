from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Zero-shot Prompting: The model is given a direct question or task

#TODO: Add a detailed background about Piyush Garg and examples of his responses to make the AI more accurate.
SYSTEM_PROMPT = """
    You are an AI Persona of Piyush Garg. You have to ans to every question as if you are
    Piyush Garg and sound natual and human tone. Use the below examples to understand how Piyush Talks
    and a background about him.

    Background
    

    Examples
     Atleast 50-80 examples
"""


messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

query = input("> ") # User input for the chatbot
messages.append({"role": "user", "content": query})

while True:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    
    answer = response.choices[0].message.content
    print(answer)
    
    # Append the AI's response to the messages for context in the next round
    messages.append({"role": "assistant", "content": answer})
    
    # Get the next user input
    query = input("> ")
    messages.append({"role": "user", "content": query})