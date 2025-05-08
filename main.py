from utils.data_fetcher import fetch_ohlc
from strategies.price_action import detect_signals
from backtesting.backtest import BacktestStrategy
import backtrader as bt


def main():
    # Fetch 5-minute data
    df = fetch_ohlc(timeframe=mt5.TIMEFRAME_M5, bars=1000)

    # Generate signals
    df = detect_signals(df)

    # Backtest
    cerebro = bt.Cerebro()
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(BacktestStrategy)
    cerebro.run()
    cerebro.plot()


if __name__ == "__main__":
    main()