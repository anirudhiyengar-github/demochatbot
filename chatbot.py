
import streamlit as st

st.set_page_config(page_title="Simple AI Chatbot", page_icon="🤖")
st.title("🤖 Chat with AI")
st.caption("A simple chatbot demo you can share with your friends.")

# Initialize chat history if not yet set
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Simple bot logic (rule-based)
def bot_reply(user_input):
    user_input = user_input.lower()
    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "Hello! 👋 I'm your chatbot Anirudh . How can I help you today?"
    elif "your name" in user_input:
        return "I'm just a simple AI demo. You can name me whatever you like!"
    elif "how are you" in user_input:
        return "I'm just code, but I'm functioning perfectly! 🤖"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm still learning. Try asking me something simpler!"

# User input box
user_input = st.text_input("You:", "", key="input")

# Respond and update chat history
if st.button("Send") and user_input.strip():
    response = bot_reply(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))
    st.rerun()

# Display chat history
for speaker, message in st.session_state.chat_history:
    with st.chat_message(speaker):
        st.markdown(message)
