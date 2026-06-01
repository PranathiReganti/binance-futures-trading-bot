import argparse

from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("symbol", help="Trading Symbol (e.g. BTCUSDT)")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("order_type", help="MARKET or LIMIT")
    parser.add_argument("quantity", help="Order Quantity")
    parser.add_argument(
        "--price",
        help="Price (required for LIMIT orders)",
        required=False
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)

        price = None

        if order_type == "LIMIT":
            price = validate_price(args.price)

        client = BinanceClient().get_client()

        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n========== ORDER SUMMARY ==========")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Order ID    : {response.get('orderId')}")
        print(f"ExecutedQty : {response.get('executedQty', 'N/A')}")
        print(f"Status      : {response.get('status', 'N/A')}")
        print("===================================")
        print("✅ Order placed successfully")

    except Exception as e:

        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()