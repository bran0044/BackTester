import backtrader as bt
from decimal import Decimal
import strategy
import backtrader.feeds as btfeeds

# CEREBRO SETTINGS
cerebro = bt.Cerebro()
cerebro.broker.setcommission(commission=0.001)
cerebro.broker.set_cash(1000)
cerebro.addsizer(bt.sizers.AllInSizer, percents=95)
value_before = Decimal(cerebro.broker.getvalue())

# DATA
data = btfeeds.GenericCSVData(
    dataname='Tickers\SPY_30minute_2000-01-21_2021-11-26.csv',
    timeframe=bt.TimeFrame.Minutes, compression=30,
    nullvalue=0.0,
    dtformat=('%Y-%m-%d %H:%M:%S'),
    datetime=0,
    high=2,
    low=3,
    open=1,
    close=4,
    volume=5,
    openinterest=-1
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

print("Start Value: ", value_before)
print("End Value: ",round(float(value_after),2))
print("Gain/Loss: ",round((float(value_after) - float(value_before)),2))
print("% Gain/Loss: ",round(float(((value_after/value_before))-1)*100,2), "%")
print("------------------------")
