# Chainlit Chatbot with Gemini API

This project is a chatbot built using Chainlit and Google's Gemini API. It supports OAuth authentication via GitHub and maintains chat history during a session.

## Features
- Uses `chainlit` for chatbot interaction
- Integrates `google.generativeai` (Gemini API) for AI-generated responses
- Supports OAuth authentication via GitHub
- Maintains chat history within a user session

## Requirements
Ensure you have the following installed:
- Python 3.8+
- Required dependencies (listed in `requirements.txt`)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/chainlit-gemini-chatbot.git
   cd chainlit-gemini-chatbot
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Setup
1. Create a `.env` file and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
2. Run the chatbot:
   ```sh
   chainlit run app.py
   ```

## Usage
- Start the chatbot and interact with it through Chainlit’s UI.
- The chatbot will generate responses using Gemini API and maintain chat history during a session.
- OAuth authentication via GitHub is enabled for secure user access.

## License
This project is licensed under the MIT License.
