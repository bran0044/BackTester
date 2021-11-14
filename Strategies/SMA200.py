from datetime import datetime
import backtrader as bt
import matplotlib

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma200 = bt.ind.SMA(period=200)
        price = self.data
        crossover = bt.ind.CrossOver(sma200,price)
        self.signal_add(bt.SIGNAL_LONG, crossover)