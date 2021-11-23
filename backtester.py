import backtrader as bt
from decimal import Decimal
import strategy

# CEREBRO SETTINGS
cerebro = bt.Cerebro()
cerebro.broker.setcommission(commission=0.001)
cerebro.broker.set_cash(1000)
cerebro.addsizer(bt.sizers.AllInSizer, percents=95)
value_before = Decimal(cerebro.broker.getvalue())

# DATA
data = bt.feeds.GenericCSVData(
        dataname='replaced - TradingView\\msft-15m-rep.csv',
        timeframe=bt.TimeFrame.Minutes,
        compression=15,
        dtformat='%Y-%m-%d %H:%M',
        tmformat='%H:%M',

    )


# INSERT STRATEGY
strategy = strategy.strategy

# Runs and plots strategy
cerebro.addstrategy(strategy)
cerebro.adddata(data)
result = cerebro.run()
cerebro.plot()
results = cerebro.run()
results = results[0]
# Prints value in console
value_after = Decimal(cerebro.broker.getvalue())
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='mysharpe')
print("------------------------")
print('Sharpe Ratio:', results.analyzers.mysharpe.get_analysis())

print("Start Value: ", value_before)
print("End Value: ",round(float(value_after),2))
print("Gain/Loss: ",round((float(value_after) - float(value_before)),2))
print("% Gain/Loss: ",round(float(((value_after/value_before))-1)*100,2), "%")
print("------------------------")
