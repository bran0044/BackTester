import requests
date = []
open = []
high = []
low = []
close = []
volume = []

def lists_stocks(ticker,timeframe):
    auth = requests.get('https://financialmodelingprep.com/api/v3/historical-chart/{}/{}?apikey=a695b9febb89a33c6e4362da9ffcdf5b'.format(timeframe,ticker))
    fmp = auth.json()

    for x in range(len(fmp)):
        date.append(fmp[x]['date'])
        open.append(fmp[x]['open'])
        high.append(fmp[x]['high'])
        low.append(fmp[x]['low'])
        close.append(fmp[x]['close'])
        volume.append(fmp[x]['volume'])