# debug/print
def printPrices(pricesForPrinting):
    for stock in pricesForPrinting:
        print(stock)
        historicalPrices = pricesForPrinting[stock]
        for historicalPrice in historicalPrices:
            print(historicalPrice)

def printPriceSpot(pricesForPrinting):
    for stock in pricesForPrinting:
        print(stock)
        spotPrice = pricesForPrinting[stock]
        print(spotPrice)