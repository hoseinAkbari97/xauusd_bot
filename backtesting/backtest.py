# backtesting/backtest.py
import backtrader as bt

class BacktestStrategy(bt.Strategy):
    params = (('risk_percent', 0.01),)

    def __init__(self):
        self.signal = self.datas[0].lines.signal  # <-- Access via .lines.signal

    def next(self):
        if self.signal[0] == 1:
            size = self.broker.getvalue() * self.p.risk_percent / self.data.close[0]
            self.buy(size=size)
        elif self.signal[0] == -1:
            self.sell()