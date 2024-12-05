import gradio as gr
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os

load_dotenv()

project_connection_string = os.getenv("PROJECT_CONNECTION_STRING")

project = AIProjectClient.from_connection_string(
    conn_str=project_connection_string, credential=DefaultAzureCredential()
)

chat = project.inference.get_chat_completions_client()

# Initialize conversation with system message
system_message = {
    "role": "system",
    "content": "You are an AI assistant that only answers question about Microsoft azure. You have a temper and you are a bit rude but professional. Don't answer anything that is not Azure related.",
}
conversation = [system_message]

def chat_with_ai(user_input, history=[]):
    conversation.append({"role": "user", "content": user_input})

    response = chat.complete(
        model="gpt-4o-mini",
        messages=conversation,
        temperature=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )
    reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})

    history.append((user_input, reply))
    return history

iface = gr.Interface(
    fn=chat_with_ai,
    inputs="text",
    outputs="chatbot",
    title="AI Assistant Chat",
    description="Chat with an azure AI assistant.",
)

iface.launch()