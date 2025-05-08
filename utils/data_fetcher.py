import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta


def fetch_ohlc(symbol="XAUUSD", timeframe=mt5.TIMEFRAME_M5, bars=1000):
    if not mt5.initialize():
        print("MT5 initialization failed!")
        return None

    try:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
        if rates is None:
            print("Failed to fetch rates")
            return None

        # Debug: Print raw columns from MT5
        print("Raw columns:", rates.dtype.names)  # Keep this FIRST

        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        df = df[['open', 'high', 'low', 'close', 'tick_volume']]
        df.rename(columns={'tick_volume': 'volume'}, inplace=True)
        return df

    finally:
        mt5.shutdown()


def fetch_ohlc_by_date(symbol="XAUUSD", timeframe=mt5.TIMEFRAME_M5, days=30):
    if not mt5.initialize():
        return None

    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        rates = mt5.copy_rates_range(symbol, timeframe, start_date, end_date)

        if not rates:
            return None

        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        return df[['open', 'high', 'low', 'close', 'tick_volume']].rename(columns={'tick_volume': 'volume'})

    finally:
        mt5.shutdown()