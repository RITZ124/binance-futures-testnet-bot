from bot.logging_config import setup_logger

logger = setup_logger("orders", "orders.log")

def place_order(
    client,
    symbol,
    side,
    order_type,
    quantity,
    price=None,
    stop_price=None
):
    try:
        client.client.futures_change_leverage(
            symbol=symbol,
            leverage=1,
            recvWindow=60000
        )

        logger.info(f"Leverage set for {symbol}")

        if order_type == "MARKET":
            order = client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
                recvWindow=60000
            )

        elif order_type == "LIMIT":
            order = client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
                recvWindow=60000
            )

        elif order_type == "STOP_MARKET":
            order = client.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                quantity=quantity,
                stopPrice=stop_price,
                recvWindow=60000
            )

        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Order response: {order}")
        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise