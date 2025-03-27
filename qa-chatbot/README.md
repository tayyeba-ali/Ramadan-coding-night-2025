# LLM Powered QA Chatbot using Python, UV, Chainlit, and Gemini

## Overview
This project is a Question-Answering (QA) chatbot powered by a Large Language Model (LLM) using Google's Gemini API. The chatbot is built with Python, UV, and Chainlit, enabling real-time conversational AI capabilities.

## Technologies Used
- **Python**: Core programming language for the chatbot.
- **UV**: Lightweight execution environment for running Python applications.
- **Chainlit**: Framework for building conversational AI interfaces.
- **Google Gemini API**: LLM used to generate responses.
- **Dotenv**: Used to manage API keys securely.

## Installation

Ensure you have Python installed on your system. Then, follow these steps:

1. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv chatbot-env
   source chatbot-env/bin/activate  # On Windows use: chatbot-env\Scripts\activate
   ```

2. Install the required dependencies:
   ```sh
   pip install chainlit google-generativeai python-dotenv uv
   ```

3. Set up your API key:
   - Create a `.env` file in the project directory and add the following line:
     ```sh
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

### Running the Chatbot with Chainlit

1. Save the following code as `app.py`:
   ```python
   import os
   import chainlit as cl
   import google.generativeai as genai
   from dotenv import load_dotenv

   load_dotenv()

   gemini_api_key = os.getenv("GEMINI_API_KEY")

   genai.configure(api_key=gemini_api_key)

   model = genai.GenerativeModel(model_name="gemini-2.0-flash")

   @cl.on_chat_start
   async def handle_chat_start():
       await cl.Message(content="Hello! How can I help you today?").send()

   @cl.on_message
   async def handle_message(message: cl.Message):
       prompt = message.content
       response = model.generate_content(prompt)
       response_text = response.text if hasattr(response, "text") else ""
       await cl.Message(content=response_text).send()
   ```

2. Run the chatbot:
   ```sh
   chainlit run app.py
   ```

3. Open the provided URL in your browser to interact with the chatbot.

### Running the Chatbot in CLI

1. Save the following code as `cli_chatbot.py`:
   ```python
   import os
   import google.generativeai as genai
   from dotenv import load_dotenv

   load_dotenv()

   genai.configure(api_key=os.environ["GEMINI_API_KEY"])

   model = genai.GenerativeModel(model_name="gemini-2.0-flash")

   while True:
       user_input = input("\nEnter your question (or 'quit' to exit): ")

       if user_input.lower() == "quit":
           print("Thanks for chatting! Goodbye!")
           break

       response = model.generate_content(user_input)
       print(f"\nAI: {response.text}")
   ```

2. Run the chatbot in the terminal:
   ```sh
   python cli_chatbot.py
   ```

3. Type your questions in the console and receive AI-generated responses.

## Features
- Real-time interaction with an LLM-powered chatbot.
- Two modes: Web-based (Chainlit) and CLI-based.
- Secure API key handling with dotenv.

## Future Enhancements
- Enhance UI for better user experience.
- Implement memory-based conversation handling.
- Add integration with external APIs for broader functionalities.

## License
This project is open-source and available under the MIT License.