# Simple Agent using UV, OpenAI Agents SDK, and Gemini

## Overview
This project implements a simple AI agent using UV, OpenAI Agents SDK, and Gemini to create a Greeting Agent. The agent is designed to respond with specific greetings based on user input.

## Features
- Responds with **Salam** when greeted with "hi"
- Replies with **Allah Hafiz** when the user says "bye"
- If the user asks anything unrelated to greetings, it responds with a message saying it only handles greetings

## Technologies Used
- Python
- [UV](https://github.com/continuum-io/uv)
- OpenAI Agents SDK
- Gemini API
- dotenv (for environment variable management)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/simple-agent.git
   cd simple-agent
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add your Gemini API key:
     ```env
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage
Run the script using:
```sh
python main.py
```
Enter your input when prompted, and the agent will respond accordingly.

## Code Explanation
```python
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

# Load environment variables
load_dotenv()

# Retrieve API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Set up OpenAI provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

# Define the agent with instructions
agent = Agent(
    name="Greeting Agent",
    instructions=(
        "You are a Greeting Agent. Your task is to greet the user with a friendly message. "
        "When someone says 'hi', reply with 'Salam from Tayyeba Ali'. "
        "If someone says 'bye', reply with 'Allah Hafiz from Tayyeba Ali'. "
        "For any other query, respond with 'Tayyeba is here just for greeting. I can't answer anything else, sorry.'"
    ),
    model=model,
)

# Get user input and generate a response
user_question = input("Enter your question: ")
result = Runner.run_sync(agent, user_question)
print(result.final_output)
```

## Contribution
Feel free to fork this repository and contribute by submitting a pull request.

## License
This project is licensed under the MIT License.

## Author
Tayyeba Ali

