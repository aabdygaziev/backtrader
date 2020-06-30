import requests, json
import pandas as pd

url = url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&outputsize=full&apikey=LX71H2XX0HSO5PAO'

r = requests.get(url)
data = json.loads(r.content)['Time Series (Daily)']

df = pd.DataFrame(data)
pd.to_datetime(df.columns)

df = df.transpose().set_index(df.columns)
df.to_csv('TSLA.csv')