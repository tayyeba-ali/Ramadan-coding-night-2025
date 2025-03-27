# Simple Chatbot using Python, UV, and Chainlit

## Overview
This project is a simple chatbot built using Python, UV, and Chainlit. The chatbot echoes back user messages, demonstrating basic conversational capabilities with minimal setup.

## Technologies Used
- **Python**: The core programming language for the chatbot.
- **UV**: Lightweight execution environment for running Python web applications.
- **Chainlit**: A framework for building conversational AI interfaces.

## Installation

Ensure you have Python installed on your system. Then, follow these steps:

1. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv chatbot-env
   source chatbot-env/bin/activate  # On Windows use: chatbot-env\Scripts\activate
   ```

2. Install the required dependencies:
   ```sh
   pip install chainlit uv
   ```

## Usage

1. Save the following code as `app.py`:
   ```python
   import chainlit as cl

   @cl.on_message
   async def main(message: cl.Message):
       response = f"You said: {message.content}"
       await cl.Message(content=response).send()
   ```

2. Run the chatbot:
   ```sh
   chainlit run app.py
   ```

3. Open the provided URL in your browser to interact with the chatbot.

## Features
- Simple echo response
- Real-time interaction
- Lightweight and easy to deploy

## Future Enhancements
- Implement NLP-based responses
- Add integration with external APIs
- Improve UI for better user experience

## License
This project is open-source and available under the MIT License.

