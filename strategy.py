import backtrader as bt


class strategy(bt.SignalStrategy):
    params = dict(
        stop_loss=0.05,  # price is 2% less than the entry point
        trail=False,
    )
    def __init__(self):
        price = self.data
        self.order = None

        # MACD
        self.macd = bt.indicators.MACD(self.data, period_me1=12, period_me2=26, period_signal=9)

        # Moving Averages
        self.ema = bt.ind.EMA(period=7)
        self.sma = bt.ind.SMA(period=25)

        # RSI
        self.rsi = bt.ind.RSI(period=50)

        # Crosses
        self.cross = bt.ind.CrossOver(self.sma, self.data)
        #self.signal_add(bt.SIGNAL_LONG, self.cross)

        return

# 16.04%

    def next(self):
        if not self.position:
            return
        if self.position:
            return

'''    def notify_order(self, order):
        if not order.status == order.Completed:
            return  # discard any other notification
        if not self.position:  # we left the market
            return
        if not self.p.trail:
            stop_price = order.executed.price * (1.0 - self.p.stop_loss)
            self.sell(exectype=bt.Order.Stop, price=stop_price)
        else:
            self.sell(exectype=bt.Order.StopTrail, trailamount=self.p.trail)
        return'''
