from datetime import datetime
import backtrader as bt
import matplotlib

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma50 = bt.ind.SMA(period=50)
        price = self.data
        crossover = bt.ind.CrossOver(sma50,price)
        self.signal_add(bt.SIGNAL_LONG, crossover)