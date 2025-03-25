# Random Joke Generator

This is a simple Random Joke Generator built using Streamlit and Python. It fetches a random joke from the [Official Joke API](https://official-joke-api.appspot.com/) and displays it on the web app.

## Features
- Fetches a random joke from the API
- Displays the joke in an interactive UI
- Built with Streamlit for a lightweight and easy-to-use web interface

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/tayyeba-ali/random-joke-generator.git
   cd random-joke-generator
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the Streamlit app with:
```bash
streamlit run app.py
```

## Dependencies
- `streamlit`
- `requests`

## How It Works
1. The app fetches a random joke from the Official Joke API.
2. When the user clicks the **"Tell me a joke"** button, a joke is displayed.
3. A fallback joke is provided in case of API failure.

## Contributing
Feel free to fork this repository and make improvements. Pull requests are welcome!

## Credits
Built with ❤️ by [Tayyeba Ali](https://github.com/tayyeba-ali).

## License
This project is open-source and available under the [MIT License](LICENSE).