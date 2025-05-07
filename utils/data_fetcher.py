import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta


def fetch_ohlc(symbol="XAUUSD", timeframe=mt5.TIMEFRAME_M5, bars=1000):
    """
    Fetch OHLC data for XAUUSD.

    Parameters:
    - timeframe: MT5 timeframe (e.g., mt5.TIMEFRAME_M5 for 5-minute data)
    - bars: Number of recent bars to fetch (max 1000 for copy_rates_from_pos)
    """
    if not mt5.initialize():
        print("MT5 not initialized!")
        return None

    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    mt5.shutdown()

    if rates is None:
        return None

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    df = df[['open', 'high', 'low', 'close', 'volume']]
    return df


def fetch_ohlc_by_date(symbol="XAUUSD", timeframe=mt5.TIMEFRAME_M5, days=30):
    """
    Fetch OHLC data for a specific date range.
    Example: Last 30 days of 5-minute data.
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    if not mt5.initialize():
        return None

    rates = mt5.copy_rates_range(symbol, timeframe, start_date, end_date)
    mt5.shutdown()

    if not rates:
        return None

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    return df[['open', 'high', 'low', 'close', 'volume']]

print("Hello. This is the first XAUUSD bot for 5 min trade")