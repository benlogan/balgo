# price data analysis - look for stable or consistently rising prices
def analysisAlwaysRising(pricesForAnalysis):
    print("Starting Data Analysis : analysisAlwaysRising")
    for stock in pricesForAnalysis:
        #print(stock)
        historicalPrices = pricesForAnalysis[stock]

        # Iterating using while loop
        length = len(historicalPrices)
        i = 0
        previousPrice = 0

        # or at least not falling, otherwise we are going to ignore a lot!
        pricesAreRising = False

        while i < length:
            if i == 0:
                # previousPrice = historicalPrice[i]
                # nothing else to do - no analysis
                x = 0
            else:
                # do some basic analysis
                latestPrice = historicalPrices[i]
                if latestPrice >= previousPrice:
                    pricesAreRising = True
                    #print('FOUND A HIGHER PRICE : ' + stock + " : " + str(latestPrice))
                else:
                    pricesAreRising = False
                    break
            previousPrice = historicalPrices[i]
            i += 1

        if pricesAreRising:
            print('CONSISTENTLY RISING PRICES : ' + stock)
            print('PRICE HISTORY...');
            for historicalPrice in historicalPrices:
                print(historicalPrice)
    print("Ending Data Analysis")