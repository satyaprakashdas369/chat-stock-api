import re

def parse_message(message: str):
    message = message.lower()

    # Intent detection
    if "stock" in message or "available" in message:
        intent = "check_stock"
    elif "price" in message or "rate" in message:
        intent = "check_price"
    else:
        intent = "unknown"

    # Quantity extraction
    qty_match = re.search(r'\d+', message)
    quantity = int(qty_match.group()) if qty_match else None

    return intent, quantity