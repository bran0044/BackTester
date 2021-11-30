import backtrader as bt

class strategy(bt.SignalStrategy):
    def __init__(self):
        price = self.data
        self.order = None

        # MACD
        self.macd = bt.indicators.MACD(self.data, period_me1=12, period_me2=26, period_signal=9)

        # Moving Averages
        self.ema = bt.ind.EMA(period=7)
        self.sma = bt.ind.SMA(period=50)

        # RSI
        self.rsi = bt.ind.RSI(period=50)

        # Crosses
        self.cross = bt.ind.CrossOver(self.sma, self.data)
        self.signal_add(bt.SIGNAL_LONG, self.cross)
        return

    def next(self):
        if not self.position:
            return
        if self.position:
            return