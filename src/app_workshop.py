# ----------------- Step 1: Imports -----------------
import streamlit as st
from together import Together
import random

# ----------------- Step 2: Page Configuration -----------------
# TODO: Set Streamlit page title, icon, and layout using st.set_page_config
# Hint: search "streamlit set_page_config example"
# You can safely set your API key here
together_api_key = "48dfc1d32e9f36721e7a290863019522cd352e0e9cc671d16447ac408988bd15"
client = Together(api_key=together_api_key)

st.set_page_config(page_title="Together AI Chatbot", page_icon="🤖", layout="centered")


# ----------------- Step 3: Page Styling -----------------
# TODO: Add custom CSS to:
# - Set background color for the app
# - Widen the central content area
# - Style the chat input area
# Hint: Use st.markdown with unsafe_allow_html=True
# Search: "streamlit custom css background color"


# ----------------- Step 4: App Title -----------------
# TODO: Add a fun app title using st.title
# Hint: Search "streamlit st.title example"
st.title("🤖 Together AI Chatbot")


# ---------------- Sidebar - Settings ---------------- #
# TODO: Create sidebar using st.sidebar
# Hint: search "streamlit st.sidebar components"
st.sidebar.header("🛠️ Settings")


# --------- Model Selection ---------
# TODO: Add dropdown to choose the model using st.sidebar.selectbox
# Hint: Search "streamlit st.sidebar selectbox example"


# --------- Chat Style Selection ---------
# TODO: Add radio buttons to choose chat style using st.sidebar.radio
# Hint: Search "streamlit sidebar radio button"


# ----------------- Step 5: Chat History Initialization -----------------
# TODO: Use st.session_state to store message history
# Hint: Search "streamlit st.session_state tutorial"


# ----------------- Step 6: Surprise Me Button -----------------
# TODO: Add button to inject a random prompt using st.sidebar.button
# Hint: Search "streamlit sidebar button"
# Bonus: Use random.choice for prompt selection


# ----------------- Step 7: LLM Parameter Presets -----------------
# TODO:
# - Use st.sidebar.radio to choose between "Custom", "Default", etc.
# - If "Custom", show sliders for Temperature & Top-p using st.sidebar.slider
# Hint: Search "streamlit slider example"


# ----------------- Step 8: Other LLM Controls -----------------
# TODO: Show sliders for:
# - Max Tokens
# - Frequency Penalty
# - Presence Penalty
# - Repetition Penalty
# Hint: Search "streamlit slider range example"


# ----------------- Step 9: Prompt Engineering Tips -----------------
# TODO: Use st.sidebar.expander to show tips
# Hint: Search "streamlit sidebar expander example"


# ----------------- Step 10: Last Token Usage (Optional) -----------------
# TODO: Display last token usage with st.sidebar.info if available
# Hint: Search "streamlit sidebar info box"


# ---------------- Chat Interface ---------------- #

# --------- Display Chat History ---------
# TODO: Loop through st.session_state.messages
# Use st.chat_message to display each message
# Hint: Search "streamlit st.chat_message example"


# ----------------- Step 11: User Input Section -----------------
# TODO: Use st.chat_input to capture user message
# Hint: Search "streamlit st.chat_input"


# --------- Surprise Prompt Handling ---------
# TODO: If a surprise prompt exists in session state, use it


# ----------------- Step 12: Build Final Prompt -----------------
# TODO: If a tone (e.g., Friendly) is selected, modify the user's prompt accordingly


# ----------------- Step 13: Append User Message -----------------
# TODO: Add the user message to st.session_state.messages
# Display it using st.chat_message


# ----------------- Step 14: Assistant Response -----------------
# TODO:
# - Show "Thinking..." placeholder
# - Send request to Together AI using client.chat.completions.create
# - Pass the selected model, prompt, and parameters
# - Get assistant's response
# - Handle errors with try/except
# - Display response
# - Save response to chat history


# ---------------- END OF APP ---------------- #
