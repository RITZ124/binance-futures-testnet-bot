# bot/validators.py
def validate_inputs(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("quantity must be > 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("price is required for LIMIT order")