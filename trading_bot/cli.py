# cli.py
import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import validate_inputs

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate_inputs(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    client = BinanceFuturesClient()

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Summary")
    print("-" * 30)
    print(f"Order ID: {order.get('orderId')}")
    print(f"Status: {order.get('status')}")
    print(f"Executed Qty: {order.get('executedQty')}")
    print(f"Avg Price: {order.get('avgPrice', 'N/A')}")
    print("SUCCESS")

if __name__ == "__main__":
    main()