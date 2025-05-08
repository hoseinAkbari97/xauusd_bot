import backtrader as bt
import pandas as pd

class BacktestStrategy(bt.Strategy):
    params = (('risk_percent', 0.01),)

    def __init__(self):
        self.data_close = self.datas[0].close
        self.signal = self.datas[0].signal

    def next(self):
        if self.signal[0] == 1:  # Buy
            size = self.broker.getvalue() * self.p.risk_percent / self.data_close[0]
            self.buy(size=size)
        elif self.signal[0] == -1:  # Sell
            self.sell()