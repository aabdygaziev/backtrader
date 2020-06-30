import backtrader as bt
import datetime
from strategies import TestStrategy
import matplotlib.pyplot as plt

cerebero = bt.Cerebro()
cerebero.addstrategy(TestStrategy)

data = bt.feeds.YahooFinanceCSVData(
		dataname='TSLA.csv',
		reverse = True
)

cerebero.broker.set_cash(1000)
cerebero.adddata(data)
cerebero.addsizer(bt.sizers.FixedSize, stake=10)
cerebero.broker.setcommission(commission=0.001)

print('Starting portfolio value: %.2f' % cerebero.broker.getvalue())
cerebero.run()
print('Ending portfolio value: %.2f' % cerebero.broker.getvalue())
