import backtrader as bt


class strategy(bt.SignalStrategy):
    params = dict(
        stop_loss=0.15,
        trail=False)

    params = (
        # Standard MACD Parameters
        ('macd1', 8),
        ('macd2', 21),
        ('macdsig', 5))

    # SETUP PRIMARY
    def __init__(self):
        price = self.data
        self.order = None

        # INDICATORS
        self.ema1 = bt.ind.SMA(period=14)
        self.ema2 = bt.ind.SMA(period=30)
        self.fractal = bt.studies.Fractal(period=5, bardist=0.016, shift_to_potential_fractal=2)
        self.macd = bt.indicators.MACD(self.data,
                                       period_me1=12,
                                       period_me2=26,
                                       period_signal=9)

        # Cross of macd.macd and macd.signal
        self.mcross = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)
        self.cross = bt.ind.CrossOver(self.ema1,self.ema2)

        return

    def next(self):
        if not self.position:
            #INSERT BUY SIGNAL
            return
        if self.position:
            #INSERT SELL SIGNAL
            return

    # STOP LOSS
    def notify_order(self, order):
        return
