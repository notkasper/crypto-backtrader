import backtrader as bt
import datetime as dt
from strategies import MyStrategy

cerebro = bt.Cerebro()

cerebro.broker.set_cash(100000)

data = bt.feeds.YahooFinanceCSVData(
    dataname="src/data/oracle.csv",
    fromdate=dt.datetime(2000, 1, 1),
    todate=dt.datetime(2000, 12, 31),
    reverse=False
)

cerebro.adddata(data)

cerebro.addstrategy(MyStrategy)

print('starting portfolio value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('final portfolio value: %.2f' % cerebro.broker.getvalue())
