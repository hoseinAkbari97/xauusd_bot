import pandas as pd

def detect_signals(df):
    df['SMA20'] = df['close'].rolling(20).mean()
    df['SMA50'] = df['close'].rolling(50).mean()
    df['Signal'] = 0  # 0 = No trade, 1 = Buy, -1 = Sell
    df.loc[df['SMA20'] > df['SMA50'], 'Signal'] = 1
    df.loc[df['SMA20'] < df['SMA50'], 'Signal'] = -1
    return df
