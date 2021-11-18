from datetime import datetime
import backtrader as bt
from decimal import Decimal
import Strategies.mainstrat

# CEREBRO SETTINGS
cerebro = bt.Cerebro()
cerebro.broker.setcommission(commission=0.001)
cerebro.broker.set_cash(1000)
cerebro.addsizer(bt.sizers.AllInSizer, percents=99)
value_before = Decimal(cerebro.broker.getvalue())

# DATA
data = bt.feeds.YahooFinanceCSVData(dataname='data_(daily)\\atos.csv',
                                    fromdate=datetime(2020, 1, 1),
                                    todate=datetime(2021, 1, 1))



# INSERT STRATEGY
strategy = Strategies.mainstrat.strategy

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
