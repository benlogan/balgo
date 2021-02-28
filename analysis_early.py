# look for stocks that are trending up over a period of time
# or just look for an average price rise of a certain size and only run/monitor during the opening 30 minutes
tradingStocks = {}

riseThreshold = 1 # percentage rise required to qualify for trading

def analysisAverageRising(pricesForAnalysis):

    print("Starting Data Analysis : analysisAverageRising")
    for stock in pricesForAnalysis:
        historicalPrices = pricesForAnalysis[stock]

        length = len(historicalPrices)

        startingPrice = float(historicalPrices[0])
        latestPrice = float(historicalPrices[length-1])
        priceDifference = float(latestPrice) - float(startingPrice)

        if(length > 1):
            #print(stock + ' START PRICE : ' + str(startingPrice) + ' END PRICE : ' + str(latestPrice) + ' ' + str(priceDifference))

            # if its positive, otherwise don't care
            if priceDifference > 0:
                percentageRise = round(priceDifference / startingPrice * 100, 2)
                #print('percentageRise : ' + str(percentageRise))

                if percentageRise > riseThreshold:
                    print('LARGE PERCENTAGE RISE : ' + stock + " is UP " + str(percentageRise) + "%")
                    tradingStocks[stock] = latestPrice
                    print('PRICE HISTORY...')
                    for historicalPrice in historicalPrices:
                        print(historicalPrice)
    print("Ending Data Analysis")