from openai import OpenAI #this imports Openai from the terminal.(remember to use pip install openai in terminal first or it wont work )
import os
from dotenv import load_dotenv #this helps protect your api_key from being visble in this script. remember to get pip install dotenv and creare a .env file with your api key inside 
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("Loaded key:", api_key)  # This will tell you if it's working

client = OpenAI(api_key=api_key)

print("🤖 BetaMax is ready! Type something (or type 'exit' to quit)\n") #this prints the message "Baymax is ready type something (or type quit to exit)" to terminal 

chat_history = [] #this resets chat 

while True:
    user_input = input("You: ") #this is the user input. basically ("you: user_input")

    if user_input.lower() == "exit": #this "if" section is looking for the input "exit" from user input. if true baymax says goodbye and ends task.
        print("Goodbye!")
        break

    chat_history.append({"role": "user", "content": user_input}) # This line adds what the user just said to the chat_history list. The role is "user" and the content is whatever they typed.

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    ) #this section is sending the chat history to openai so it knows the history of the conversation.

    reply = response.choices[0].message.content
    print("BetaMax:", reply)

    chat_history.append({"role": "assistant", "content": reply})


