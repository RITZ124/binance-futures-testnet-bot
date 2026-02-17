from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import (
    validate_common,
    validate_limit,
    validate_stop
)

def prompt(msg):
    return input(msg).strip()

def main():
    print("\n=== Binance Futures Testnet Trading Bot ===\n")

    symbol = prompt("Enter symbol (e.g. BTCUSDT): ").upper()
    side = prompt("Enter side (BUY / SELL): ").upper()

    print("\nOrder Types:")
    print("1. MARKET")
    print("2. LIMIT")
    print("3. STOP_MARKET")

    order_choice = prompt("Choose order type (1/2/3): ")

    quantity = float(prompt("Enter quantity: "))

    price = None
    stop_price = None

    if order_choice == "1":
        order_type = "MARKET"

    elif order_choice == "2":
        order_type = "LIMIT"
        price = float(prompt("Enter limit price: "))
        validate_limit(price)

    elif order_choice == "3":
        order_type = "STOP_MARKET"
        stop_price = float(prompt("Enter stop price: "))
        validate_stop(stop_price)

    else:
        print("Invalid order type selected")
        return

    validate_common(symbol, side, quantity)

    confirm = prompt("\nConfirm order? (yes/no): ").lower()
    if confirm != "yes":
        print("Order cancelled")
        return

    client = BinanceFuturesClient()

    order = place_order(
        client,
        symbol,
        side,
        order_type,
        quantity,
        price,
        stop_price
    )

    print("\nOrder Placed Successfully")
    print("-" * 30)
    print(f"Order ID: {order.get('orderId')}")
    print(f"Status: {order.get('status')}")
    print(f"Executed Qty: {order.get('executedQty')}")
    print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

if __name__ == "__main__":
    main()