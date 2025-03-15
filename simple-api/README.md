# FastAPI Side Hustle & Money Quotes API

This is a simple FastAPI application that provides random side hustle ideas and money-related quotes.

## Features
- Get a random side hustle idea.
- Get a random money-related quote.
- Uses API key authentication for security.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-side-hustles.git
   cd fastapi-side-hustles
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

## Running the API
Run the FastAPI application using Uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Endpoints
### Get a Random Side Hustle
**Endpoint:** `GET /side_hustles`

**Query Parameter:**
- `apiKey` (required): Your API key for authentication.

**Example Request:**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/side_hustles?apiKey=your_api_key' -H 'accept: application/json'
```

**Response:**
```json
{
  "side_hustle": "Freelancing - Start offering your skills online!"
}
```

### Get a Random Money Quote
**Endpoint:** `GET /money_quotes`

**Query Parameter:**
- `apiKey` (required): Your API key for authentication.

**Example Request:**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/money_quotes?apiKey=your_api_key' -H 'accept: application/json'
```

**Response:**
```json
{
  "money_quote": "Money is a terrible master but an excellent servant. - P.T. Barnum"
}
```

## License
This project is licensed under the MIT License.

