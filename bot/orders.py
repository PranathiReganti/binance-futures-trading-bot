from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger

logger = setup_logger()


def place_order(client, symbol, side, order_type, quantity, price=None):

    try:

        logger.info(
            f"Order Request: Symbol={symbol}, Side={side}, Type={order_type}, Quantity={quantity}, Price={price}"
        )

        if order_type == "MARKET":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Order Response: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e}")

        raise

    except Exception as e:

        logger.error(f"Unexpected Error: {e}")

        raise