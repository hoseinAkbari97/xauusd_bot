import MetaTrader5 as mt5
import pandas as pd
from dotenv import load_dotenv
import os

# Load credentials from .env
load_dotenv("config/.env")


def initialize_mt5():
    if not mt5.initialize():
        print("MT5 initialization failed:", mt5.last_error())
        return False

    # Login (optional for historical data, but required for live trading)
    authorized = mt5.login(
        login=int(os.getenv("MT5_LOGIN")),
        password=os.getenv("MT5_PASSWORD"),
        server=os.getenv("MT5_SERVER")
    )

    if authorized:
        print("Connected to MT5!")
        return True
    else:
        print("Login failed:", mt5.last_error())
        return False


initialize_mt5()
