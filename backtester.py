from datetime import datetime
import backtrader as bt
from decimal import Decimal

import Strategies.CROSSOVER
from Strategies import CROSSOVER
cerebro = bt.Cerebro()

# Starter cash
cerebro.broker.set_cash(1000)

# Allocation percentage
cerebro.addsizer(bt.sizers.AllInSizer, percents=95)

# Prints starter cash
value_before = Decimal(cerebro.broker.getvalue())

# Historical data_(daily)
data = bt.feeds.YahooFinanceData(
    dataname='data_(daily)\PCG.csv',
    fromdate=datetime(1980,1, 1),
    odate=datetime(2021, 11, 12))

# INSERT STRATEGY
strategy = Strategies.CROSSOVER.strategy

# Runs and plots strategy
cerebro.addstrategy(strategy)
cerebro.adddata(data)
cerebro.run()
cerebro.plot()

# Prints value in console
value_after = Decimal(cerebro.broker.getvalue())
print("------------------------")
print("Start Value: ", value_before)
print("End Value: ",round(float(value_after),2))
print("Gain/Loss: ",round((float(value_after) - float(value_before)),2))
print("% Gain/Loss: ",round(float(((value_after/value_before))-1)*100,2), "%")
print("------------------------")
