import cryptocompare as cc

def getPrice(num, curr):
	return "{:,}{}".format(num, curr)

both = cc.get_price(['BTC', 'ETH'], ['EUR', 'USD'])

btc = both['BTC']
eth = both['ETH']

print("-----")
print("|BTC|")
print("-----")
print("EUR ->", getPrice(btc['EUR'], "€"))
print("USD ->", getPrice(btc['USD'], "$"))

print()

print("-----")
print("|ETH|")
print("-----")
print("EUR ->", getPrice(eth['EUR'], "€"))
print("USD ->", getPrice(eth['USD'], "$"))

