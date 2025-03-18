# Time Zone App

## Overview
The **Time Zone App** is a Streamlit-based web application that allows users to view the current time in multiple time zones and convert time between different time zones.

## Features
- **View Current Time:** Select multiple time zones to see the current time in each.
- **Convert Time:** Input a specific time, select a "From" and "To" timezone, and get the converted time.
- **User-Friendly UI:** Built using Streamlit for a simple and interactive experience.

## Requirements
To run the app, make sure you have the following installed:
- Python 3.x
- Streamlit
- ZoneInfo (Python 3.9+)

## Installation
Clone the repository or create a new project folder and navigate into it:
```bash
mkdir timezone-app
cd timezone-app
```
Create a virtual environment (optional but recommended):
```bash
python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate
```
Install required dependencies:
```bash
pip install streamlit
```

## Running the App
To start the Streamlit application, run:
```bash
streamlit run app.py
```
Replace `app.py` with your script filename if different.

## Usage
1. Select multiple time zones to view the current time.
2. Use the time converter to select a time and convert it to another time zone.
3. Click the "Convert Time" button to see the converted time.

## Example Timezones Supported
- UTC
- Asia/Karachi
- America/New_York
- Europe/London
- Asia/Tokyo
- Australia/Sydney
- And more...

## Contributing
If you'd like to improve the app, feel free to fork the repository and submit a pull request with enhancements or bug fixes.

## License
This project is licensed under the MIT License.

