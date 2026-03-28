# Chat Stock API

## Overview
This project is a backend chat application that processes user messages using NLP and returns stock information.

## Tech Stack
- FastAPI
- MySQL
- SQLAlchemy
- Pandas

## Features
- Intent detection (stock / price)
- Entity extraction (item, quantity)
- MySQL database integration
- Excel-based automated testing

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Load data:
python load_data.py

3. Start server:
uvicorn main:app --reload

4. Test API:
http://127.0.0.1:8000/docs

## Example Input
{
  "message": "Do you have Android2001 vivo 50 units?"
}

## Output
Returns stock availability and details.

## Author
Satya
