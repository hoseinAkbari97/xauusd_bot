from backtesting.backtest import BacktestStrategy
from utils.data_fetcher import fetch_ohlc
from strategies.price_action import detect_signals
import backtrader as bt
import MetaTrader5 as mt5


# Test 01
class CustomData(bt.feeds.PandasData):
    lines = ('signal',)
    params = (
        ('datetime', None),
        ('open', 'open'),
        ('high', 'high'),
        ('low', 'low'),
        ('close', 'close'),
        ('volume', 'volume'),
        ('signal', 'signal'),
    )


def main():
    df = fetch_ohlc(timeframe=mt5.TIMEFRAME_M5, bars=1000)
    df = detect_signals(df)

    cerebro = bt.Cerebro()
    data = CustomData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(BacktestStrategy)
    cerebro.run()
    # cerebro.plot()


if __name__ == "__main__":
    main()