# ----------------- Step 1: Imports -----------------
import streamlit as st
from together import Together
import random
 
# Get the API key from Streamlit secrets
try:
    together_api_key = st.secrets["TOGETHER_API_KEY"]
except KeyError:
    st.error("TOGETHER_API_KEY not found. Please add it to your .streamlit/secrets.toml file.")
    st.stop()
client = Together(api_key=together_api_key)

# ----------------- Step 2: Page Configuration -----------------
# TODO: Set Streamlit page title, icon, and layout using st.set_page_config
# Hint: search "streamlit set_page_config example"
# You can safely set your API key here
st.set_page_config(page_title="Together AI Chatbot", page_icon="🤖", layout="centered")

# ----------------- Step 3: Page Styling -----------------
# TODO: Add custom CSS to:
# - Set background color for the app
# - Widen the central content area
# - Style the chat input area
# Hint: Use st.markdown with unsafe_allow_html=True
# Search: "streamlit custom css background color"

st.markdown(
    """
    <style>
    /* Set full-page background */
    [data-testid="stAppViewContainer"] {
        background-color: #ADD8E6;
    }

    /* Widen the main content area */
    .block-container {
        max-width: 90%;
        margin: 0 auto;
        padding: 1rem;
    }

    /* Style the chat input container */
    [data-testid="stChatInput"] {
        background-color: #E0F7FA;
        border: 2px solid #0288D1;
        border-radius: 10px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
# These are the available models: [
#         "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
#         "lgai/exaone-3-5-32b-instruct",
#         "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free"
#     ]

model = st.sidebar.selectbox(
    "Choose a Model",
    [
        "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "lgai/exaone-3-5-32b-instruct",
        "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free"
    ]
)


# --------- Chat Style Selection ---------
# TODO: Add radio buttons to choose chat style using st.sidebar.radio
# Hint: Search "streamlit sidebar radio button"
# These are the available styles: ["Default", "Formal", "Friendly", "Humorous", "Concise"]
tone = st.sidebar.radio(
    "Chat Style",
    ["Default", "Formal", "Friendly", "Humorous", "Concise"]
)


# ----------------- Step 5: Chat History Initialization -----------------
# TODO: Use st.session_state to store message history in "messages" variable
# Hint: Search "streamlit st.session_state tutorial"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------- Step 6: Surprise Me Button -----------------
# TODO: Add button to inject a random prompt using st.sidebar.button
# Hint: Search "streamlit sidebar button"
# Bonus: Use random.choice for prompt selection from these and store it in surprise_prompt variable:
#     random_prompts = [
#         "Explain quantum physics like I'm 5.",
#         "Tell me a joke about AI.",
#         "Give me a fun fact about space.",
#         "How do airplanes fly?",
#         "What is the meaning of life?"
#     ]

if st.sidebar.button("🎲 Surprise Me!"):
    random_prompts = [
        "Explain quantum physics like I'm 5.",
        "Tell me a joke about AI.",
        "Give me a fun fact about space.",
        "How do airplanes fly?",
        "What is the meaning of life?"
    ]
    st.session_state.surprise_prompt = random.choice(random_prompts)


# ----------------- Step 7: LLM Parameter Presets -----------------
# TODO:
# - Use st.sidebar.radio to choose between ["Custom", "Default", "Creative", "Strict"].
# - If "Custom", show sliders for Temperature & Top-p using st.sidebar.slider
# Hint: Search "streamlit slider example"

preset = st.sidebar.radio("Parameter Preset", ["Custom", "Default", "Creative", "Strict"])

if preset == "Custom":
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.01)
    top_p = st.sidebar.slider("Top-p (Nucleus Sampling)", 0.0, 1.0, 0.99, 0.01)
else:
    if preset == "Default":
        temperature = 0.7
        top_p = 0.99
    elif preset == "Creative":
        temperature = 0.9
        top_p = 0.99
    elif preset == "Strict":
        temperature = 0.2
        top_p = 0.5
    st.sidebar.write(f"Temperature: {temperature}")
    st.sidebar.write(f"Top-p: {top_p}")

# ----------------- Step 8: Other LLM Controls -----------------
# TODO: Show sliders for:
# - Max Tokens
# - Frequency Penalty
# - Presence Penalty
# - Repetition Penalty
# Hint: Search "streamlit slider range example"

max_tokens = st.sidebar.slider("Max Tokens", 100, 4096, 2048, 50)
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 2.0, 0.0, 0.01)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 2.0, 0.0, 0.01)
repetition_penalty = st.sidebar.slider("Repetition Penalty", 0.0, 2.0, 0.0, 0.01)

# ----------------- Step 9: Prompt Engineering Tips -----------------
# TODO: Use st.sidebar.expander to show these tips
# """
#     - Be specific and clear.
#     - Provide examples for better responses.
#     - Use the tone selector to control style.
#     - Experiment with temperature and top-p for creativity.
# """
# Hint: Search "streamlit sidebar expander example"

with st.sidebar.expander("💡 Prompt Engineering Tips"):
    st.markdown("""
    - Be specific and clear.
    - Provide examples for better responses.
    - Use the tone selector to control style.
    - Experiment with temperature and top-p for creativity.
    """)

# ----------------- Step 10: Last Token Usage (Optional) -----------------
# TODO: Display last token usage with st.sidebar.info if available
# Hint: Search "streamlit sidebar info box"

if 'last_token_usage' in st.session_state:
    st.sidebar.info(f"Last response used **{st.session_state.last_token_usage} tokens**")

# ---------------- Chat Interface ---------------- #

# --------- Display Chat History ---------
# TODO: Loop through st.session_state.messages
# Use st.chat_message(message["role"]) to display each (message["content"]) using st.write
# Hint: Search "streamlit st.chat_message example"
for message in st.session_state.messages:
    formatted_content = message["content"].replace("\n", "<br>")
    with st.chat_message(message["role"]):
        st.markdown(
            f"<div style='color:black; font-weight:bold'>{formatted_content}</div>",
            unsafe_allow_html=True
        )


# ----------------- Step 11: User Input Section -----------------
# TODO: Use st.chat_input to capture user message
# Hint: Search "streamlit st.chat_input"
prompt = st.chat_input("Type your message...")

# --------- Surprise Prompt Handling ---------
# TODO: If a surprise prompt exists in session state overwrite prompt variable, use it
# Then delete it

if "surprise_prompt" in st.session_state:
    prompt = st.session_state.surprise_prompt
    del st.session_state.surprise_prompt

# ----------------- Step 12: Build Final Prompt -----------------
# TODO: If a tone (e.g., Friendly) is selected, modify the user's prompt accordingly

if prompt:

    if tone != "Default":
        prompt_with_tone = f"Respond in a {tone.lower()} style:\n{prompt}"
    else:
        prompt_with_tone = prompt

# ----------------- Step 13: Append User Message -----------------
# TODO: Add the user message in this manner({"role": "user", "content": prompt_with_tone}) to st.session_state.messages
# Display it using st.chat_message("user")
    st.session_state.messages.append({"role": "user", "content": prompt_with_tone})

    formatted_prompt = prompt_with_tone.replace("\n", "<br>")
    
    with st.chat_message("user"):
        st.markdown(
            f"<div style='color:black; font-weight:bold'>{formatted_prompt}</div>",
            unsafe_allow_html=True
        )


# ----------------- Step 14: Show 'Thinking...' Placeholder -----------------
# TODO: Use st.chat_message("assistant") for assistant and st.empty to create a placeholder for the response 
# in message_placeholder variable 
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")


# ----------------- Step 15: Send Request to LLM -----------------
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            repetition_penalty=repetition_penalty
        )

        assistant_message = response.choices[0].message.content

        if hasattr(response, 'usage') and 'total_tokens' in response.usage:
            st.session_state.last_token_usage = response.usage['total_tokens']

    except Exception as e:
        assistant_message = f"⚠️ Error: {e}"

# ----------------- Step 16: Display Assistant Response -----------------
# TODO: Show assistant's message in the placeholder

    formatted_assistant_message = assistant_message.replace("\n", "<br>")
    message_placeholder.markdown(
        f"<div style='color:black; font-weight:bold'>{formatted_assistant_message}</div>",
        unsafe_allow_html=True
    )

# ----------------- Step 17: Save Assistant's Message to History -----------------
# TODO: Add assistant's message ({"role": "assistant", "content": assistant_message}) to chat history for future display

    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

# ---------------- END OF APP 😍 ---------------- #
