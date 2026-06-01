from binance.client import Client
from dotenv import load_dotenv
import os
import time


class BinanceClient:

    def __init__(self):
        load_dotenv()

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(
            self.api_key,
            self.api_secret
        )

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Auto-sync local time with Binance server
        server_time = self.client.get_server_time()
        self.client.timestamp_offset = (
            server_time["serverTime"] - int(time.time() * 1000)
        )

    def get_client(self):
        return self.client