import coinbase
import ccxt
import requests
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn



coinbase = ccxt.coinbase({
    'apiKey': 'qlnX3HHpHZcxUYAt',
    'secret': 'Pvpu3qVzCdUNXjCq18cpLjol9e3iMRR1',
})
myBitcoin = coinbase.fetch_total_balance()["BTC"]
myEthereum = coinbase.fetch_total_balance()["ETH"]

bitcoinPrice = yf.Ticker("BTC-USD")
print(bitcoinPrice.info)
hist = bitcoinPrice.history(period="5d")
print(hist)


print("This is how much Bitcoin I have: $" + str(myBitcoin))
print("This is how much Ethereum I have: $" + str(myEthereum))
# Plot everything by leveraging the very powerful matplotlib package
hist['Close'].plot(figsize=(16, 9))

