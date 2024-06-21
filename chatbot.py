# import streamlit as st
# import requests
# import json

# # Function to convert session history to messages format
# def convert_to_messages(history):
#     messages = []
#     for entry in history:
#         if entry.startswith("You:"):
#             messages.append({"role": "user", "content": entry[5:]})
#         elif entry.startswith("Bot:"):
#             messages.append({"role": "assistant", "content": entry[5:]})
#     return messages

# # Function to send request to the local model service
# def get_model_response(prompt):
#     url = "http://localhost:11434/api/chat"
#     headers = {"Content-Type": "application/json"}
#     messages = convert_to_messages(st.session_state.conversation)

#     data = {
#         "model": "gemma:2b",
#         "messages": messages,
#         "stream": False
#     }

#     response = requests.post(url, headers=headers, data=json.dumps(data))
    
#     # Print response content for debugging
#     # st.write("Response content:", response.content.decode("utf-8"))

#     try:
#         response_json = response.json()
#         return response_json['message']['content']
#     except json.JSONDecodeError as e:
#         st.error(f"JSON decode error: {e}")
#         return "Error: Invalid response from the model service."

# st.title("Chat with Local LLM")

# if 'conversation' not in st.session_state:
#     st.session_state.conversation = []

# def clear_conversation():
#     st.session_state.conversation = []

# st.button("Clear Conversation", on_click=clear_conversation)

# with st.form(key='chat_form'):
#     user_input = st.text_input("You:", "Type in a messssage here")
#     submit_button = st.form_submit_button(label='Send')

# if submit_button and user_input:
#     st.session_state.conversation.append(f"You: {user_input}")
#     print(f"Session state before bot response {st.session_state.conversation}")
#     response = get_model_response(user_input)
#     st.session_state.conversation.append(f"Bot: {response}")
#     print(f"Session state after bot response {st.session_state.conversation}")

# if st.session_state.conversation:
#     for i in range(len(st.session_state.conversation) - 1, -1, -1):
#         st.write(st.session_state.conversation[i])

import streamlit as st
import requests
import json

# Function to convert session history to messages format
def convert_to_messages(history):
    messages = []
    for entry in history:
        if entry.startswith("You:"):
            messages.append({"role": "user", "content": entry[5:]})
        elif entry.startswith("Bot:"):
            messages.append({"role": "assistant", "content": entry[5:]})
    return messages

# Function to send request to the local model service
def get_model_response(model_name, prompt):
    url = "http://localhost:11434/api/chat" if model_name == "Gemma:2b" else "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    messages = convert_to_messages(st.session_state.conversation)

    data = {
        "model": model_name,
        "messages": messages,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()
        return response_json['message']['content']
    except requests.exceptions.RequestException as e:
        st.error(f"Request error: {e}")
        return "Error: Failed to connect to the model service."
    except json.JSONDecodeError as e:
        st.error(f"JSON decode error: {e}")
        return "Error: Invalid response from the model service."

st.title("Interactive Chat with Local LLMs")

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

def clear_conversation():
    st.session_state.conversation = []

st.button("Clear Conversation", on_click=clear_conversation)

model_choice = st.selectbox("Choose the model to interact with:", ["Llama3", "Gemma:2b"])

with st.form(key='chat_form'):
    user_input = st.text_input("You:", "Type your message here")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    st.session_state.conversation.append(f"You: {user_input}")
    response = get_model_response(model_choice, user_input)
    st.session_state.conversation.append(f"Bot: {response}")

if st.session_state.conversation:
    st.write("## Conversation")
    for i in range(len(st.session_state.conversation) - 1, -1, -1):
        if st.session_state.conversation[i].startswith("You:"):
            st.markdown(f"**{st.session_state.conversation[i]}**")
        else:
            st.markdown(st.session_state.conversation[i])