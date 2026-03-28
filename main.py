from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal
from models import Item
from nlp import parse_message

app = FastAPI(title="Chat Stock API")

# Request model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    db = SessionLocal()

    try:
        message = request.message
        intent, quantity = parse_message(message)

        # Find item
        item = None
        items = db.query(Item).all()

        for i in items:
            if i.name.lower() in message.lower():
                item = i
                break

        # If item not found
        if not item:
            return {
                "intent": intent,
                "message": "Item not found"
            }

        # Response
        response = {
            "intent": intent,
            "item": item.name,
            "stock": item.stock
        }

        if quantity:
            response["requested_qty"] = quantity
            response["available"] = item.stock >= quantity

        return response

    finally:
        db.close()