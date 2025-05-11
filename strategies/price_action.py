# strategies/price_action.py
import pandas as pd

def detect_signals(df):
    df['SMA20'] = df['close'].rolling(20).mean()
    df['SMA50'] = df['close'].rolling(50).mean()
    df['signal'] = 0
    df.loc[df['SMA20'] > df['SMA50'], 'signal'] = 1
    df.loc[df['SMA20'] < df['SMA50'], 'signal'] = -1
    return df