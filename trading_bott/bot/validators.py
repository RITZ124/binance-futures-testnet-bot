def validate_common(symbol, side, quantity):
    if not symbol:
        raise ValueError("Symbol cannot be empty")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_limit(price):
    if price is None or price <= 0:
        raise ValueError("Price must be provided for LIMIT orders")


def validate_stop(stop_price):
    if stop_price is None or stop_price <= 0:
        raise ValueError("Stop price must be provided for STOP-MARKET orders")