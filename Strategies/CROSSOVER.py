from datetime import datetime
import backtrader as bt
in_position = False

class strategy(bt.SignalStrategy):
    def __init__(self):
        price = self.data
        ema1 = bt.ind.EMA(period=14)
        sma1 = bt.ind.SMA(period=50)

        #CrossOver(1, 2), buy when 1 is above 2, and sell when 1 is bellow 2.
        crossover = bt.ind.CrossOver(ema1, sma1)
        self.signal_add(bt.SIGNAL_LONG, crossover)