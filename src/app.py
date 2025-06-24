import streamlit as st
from together import Together
import random

# You can safely set your API key here
together_api_key = "48dfc1d32e9f36721e7a290863019522cd352e0e9cc671d16447ac408988bd15"
client = Together(api_key=together_api_key)

st.set_page_config(page_title="Together AI Chatbot", page_icon="🤖", layout="centered")

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

st.title("🤖 Together AI Chatbot")

# ---------------- Sidebar ---------------- #
st.sidebar.header("🛠️ Settings")

# Model selection
model = st.sidebar.selectbox(
    "Choose a Model",
    [
        "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "lgai/exaone-3-5-32b-instruct",
        "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free"
    ]
)

tone = st.sidebar.radio(
    "Chat Style",
    ["Default", "Formal", "Friendly", "Humorous", "Concise"]
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Surprise Me button
if st.sidebar.button("🎲 Surprise Me!"):
    random_prompts = [
        "Explain quantum physics like I'm 5.",
        "Tell me a joke about AI.",
        "Give me a fun fact about space.",
        "How do airplanes fly?",
        "What is the meaning of life?"
    ]
    st.session_state.surprise_prompt = random.choice(random_prompts)

# LLM parameter presets
preset = st.sidebar.radio("Parameter Preset", ["Custom", "Default", "Creative", "Strict"])

if preset == "Custom":
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.01)
    top_p = st.sidebar.slider("Top-p (Nucleus Sampling)", 0.0, 1.0, 1.0, 0.01)
else:
    if preset == "Default":
        temperature = 0.7
        top_p = 1.0
    elif preset == "Creative":
        temperature = 0.9
        top_p = 1.0
    elif preset == "Strict":
        temperature = 0.2
        top_p = 0.5
    st.sidebar.write(f"Temperature: {temperature}")
    st.sidebar.write(f"Top-p: {top_p}")

# Other sliders always active
max_tokens = st.sidebar.slider("Max Tokens", 100, 4096, 2048, 50)
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 2.0, 0.0, 0.01)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 2.0, 0.0, 0.01)
repetition_penalty = st.sidebar.slider("Repetition Penalty", 0.0, 2.0, 0.0, 0.01)

# print(f"Sending request with: temperature={temperature}, max_tokens={max_tokens}, top_p={top_p}, frequency_penalty={frequency_penalty}, presence_penalty={presence_penalty}, repetition_penalty={repetition_penalty}")

with st.sidebar.expander("💡 Prompt Engineering Tips"):
    st.markdown("""
    - Be specific and clear.
    - Provide examples for better responses.
    - Use the tone selector to control style.
    - Experiment with temperature and top-p for creativity.
    """)

if 'last_token_usage' in st.session_state:
    st.sidebar.info(f"Last response used **{st.session_state.last_token_usage} tokens**")

# ---------------- Chat Interface ---------------- #

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f"<span style='color:black; font-weight:bold'>{message['content']}</span>", unsafe_allow_html=True)

# Check for user input or Surprise Me
prompt = st.chat_input("Type your message...")

if "surprise_prompt" in st.session_state:
    prompt = st.session_state.surprise_prompt
    del st.session_state.surprise_prompt

if prompt:

    if tone != "Default":
        prompt_with_tone = f"Respond in a {tone.lower()} style:\n{prompt}"
    else:
        prompt_with_tone = prompt

    st.session_state.messages.append({"role": "user", "content": prompt_with_tone})

    with st.chat_message("user"):
        st.markdown(f"<span style='color:black; font-weight:bold'>{prompt_with_tone}</span>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")

    try:
        # st.sidebar.write(f"🧾 Final LLM Settings:")
        # st.sidebar.write(f"Temperature: {temperature}")
        # st.sidebar.write(f"Max Tokens: {max_tokens}")
        # st.sidebar.write(f"Top-p: {top_p}")
        # st.sidebar.write(f"Frequency Penalty: {frequency_penalty}")
        # st.sidebar.write(f"Presence Penalty: {presence_penalty}")
        # st.sidebar.write(f"Repetition Penalty: {repetition_penalty}")

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

    message_placeholder.markdown(f"<span style='color:black; font-weight:bold'>{assistant_message}</span>", unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})


# import streamlit as st
# from langchain_core.messages import AIMessage, HumanMessage
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate


# load_dotenv()

# # app config
# st.set_page_config(page_title="Streaming bot", page_icon="🤖")
# st.title("Streaming bot")

# def get_response(user_query, chat_history):

#     template = """
#     You are a helpful assistant. Answer the following questions considering the history of the conversation:

#     Chat history: {chat_history}

#     User question: {user_question}
#     """

#     prompt = ChatPromptTemplate.from_template(template)

#     llm = ChatOpenAI()
        
#     chain = prompt | llm | StrOutputParser()
    
#     return chain.stream({
#         "chat_history": chat_history,
#         "user_question": user_query,
#     })

# # session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [
#         AIMessage(content="Hello, I am a bot. How can I help you?"),
#     ]

    
# # conversation
# for message in st.session_state.chat_history:
#     if isinstance(message, AIMessage):
#         with st.chat_message("AI"):
#             st.write(message.content)
#     elif isinstance(message, HumanMessage):
#         with st.chat_message("Human"):
#             st.write(message.content)

# # user input
# user_query = st.chat_input("Type your message here...")
# if user_query is not None and user_query != "":
#     st.session_state.chat_history.append(HumanMessage(content=user_query))

#     with st.chat_message("Human"):
#         st.markdown(user_query)

#     with st.chat_message("AI"):
#         response = st.write_stream(get_response(user_query, st.session_state.chat_history))

#     st.session_state.chat_history.append(AIMessage(content=response))
