from openai import OpenAI
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("Loaded key:", api_key)  # This will tell you if it's working

client = OpenAI(api_key=api_key)

print("🤖 BetaMax is ready! Type something (or type 'exit' to quit)\n")

chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    reply = response.choices[0].message.content
    print("BetaMax:", reply)

    chat_history.append({"role": "assistant", "content": reply})


