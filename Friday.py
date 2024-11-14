import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load and display the image
image = Image.open("Friday.png")
st.markdown("""
    <h1 style="font-family: 'Courier New', Courier, monospace; color: #4CAF50; text-align: center;">
         FridayAI - Your Smart Assistant 
    </h1>
""", unsafe_allow_html=True)
#st.title("FridayAI")
st.image(image)

# Configure Generative AI model
genai.configure(api_key="AIzaSyCV8EP2e969dzvszNikNJyIhxkE_yxs9SA")
llm = genai.GenerativeModel("models/gemini-1.5-flash")

# Initialize the chat history and the model
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chatbot = llm.start_chat(history=[])

# Display AI greeting
st.chat_message("ai").write("𝗛𝗲𝘆! 𝗜'𝗺 𝗙𝗿𝗶𝗱𝗮𝘆, 𝘆𝗼𝘂𝗿 𝘀𝗺𝗮𝗿𝘁 𝗔𝗜. 𝗛𝗼𝘄 𝗰𝗮𝗻 𝗜 𝗵𝗲𝗹𝗽 you")

# Sidebar for chat history
st.sidebar.title("Chat History")
if st.session_state.chat_history:
    for i, (role, text) in enumerate(st.session_state.chat_history):
        st.sidebar.write(f"**{i + 1}. {role.capitalize()}**: {text}")

# Input from the user
human_prompt = st.chat_input("Say Something...")

if human_prompt:
    # Append human message to chat history
    st.session_state.chat_history.append(("human", human_prompt))
    st.chat_message("human").write(human_prompt)
    
    # Generate AI response
    response = chatbot.send_message(human_prompt)
    st.session_state.chat_history.append(("ai", response.text))
    st.chat_message("ai").write(response.text)
