# 🤖 Together AI Chatbot with Streamlit

This project is a versatile and customizable chatbot interface built with Streamlit that connects to various large language models (LLMs) through the Together AI API. It allows users to interact with different models, fine-tune generation parameters, and customize the chat experience.

## ✨ Features

- **Interactive Chat Interface**: A clean and user-friendly chat window to interact with the AI.
- **Model Selection**: Easily switch between different powerful LLMs available on the Together AI platform, such as Llama 3.3, Exaone, and DeepSeek.
- **Customizable Chat Style**: Adjust the AI's tone with presets like Formal, Friendly, Humorous, or Concise.
- **Advanced Parameter Tuning**:
    - Use presets (Default, Creative, Strict) for quick setup.
    - Manually adjust parameters like Temperature, Top-p, Max Tokens, Frequency Penalty, Presence Penalty, and Repetition Penalty for fine-grained control over the model's output.
- **"Surprise Me!" Button**: Get a random, interesting prompt to start a conversation.
- **Token Usage Display**: Keep track of the token count for the last generated response.
- **Prompt Engineering Tips**: A handy guide in the sidebar to help you write better prompts.
- **Custom Theming**: A pleasant, custom-styled interface.

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Prerequisites

- Python 3.8 or higher
- A Together AI API Key. You can get one from the [Together AI website](https://api.together.ai/).

### 2. Clone the Repository (if you haven't already)

```bash
git clone <repository-url>
cd <repository-directory>
```

### 3. Install Dependencies

Install the packages:

```bash
pip install -r requirements.txt
```
Configure Your API Key. This app uses Streamlit's secrets management to keep your API key secure. In the root directory of the project, create a new folder named .streamlit. Inside the .streamlit folder, create a new file named secrets.toml. Open secrets.toml and add your Together AI API key in the following format:
in .streamlit/secrets.toml put
TOGETHER_API_KEY = "Your-API-Key-Here"


Once you have installed the required packages, you can run the app by running the following command in your terminal:

```bash
streamlit run src/app.py
```

This will start the Streamlit app, and you will be able to interact with the chatbot in your web browser.

## Contributing

This repository is intended only for educational purposes. The only contributions that will be accepted are those that fix typos or inconsistencies with the tutorial. 

## License

This repository is licensed under the MIT License. See the [LICENSE](./LICENCE.md) file for more information.
