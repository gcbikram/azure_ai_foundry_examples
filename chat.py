from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.inference.prompts import PromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()

project_connection_string = os.getenv("PROJECT_CONNECTION_STRING")

project = AIProjectClient.from_connection_string(
    conn_str=project_connection_string, credential=DefaultAzureCredential()
)

chat = project.inference.get_chat_completions_client()

if __name__ == "__main__":
    system_message = {
        "role": "system",
        "content": "You are an AI assistant that speaks like a techno punk rocker from 2350. Be cool but not too cool. Ya dig?",
    }
    conversation = [system_message]

    print("Welcome to the AI assistant! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        conversation.append({"role": "user", "content": user_input})

        response = chat.complete(
            model="gpt-4o-mini",
            messages=conversation,
            temperature=1,
            frequency_penalty=0.5,
            presence_penalty=0.5,
        )
        reply = response.choices[0].message.content
        print(f"AI: {reply}")
        conversation.append({"role": "assistant", "content": reply})