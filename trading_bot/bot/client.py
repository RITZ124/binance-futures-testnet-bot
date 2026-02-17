# bot/client.py
import os
import time
from binance.client import Client

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET"),
            testnet=True
        )

        # Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        # ---- TIMESTAMP SYNC ----
        server_time = self.client.get_server_time()["serverTime"]
        local_time = int(time.time() * 1000)
        self.client.timestamp_offset = server_time - local_time

        # ---- GLOBAL recvWindow (CRITICAL) ----
        self.client.RECV_WINDOW = 60000