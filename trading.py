import math

traded = {}

def trade(hour, minute, tradingStocks):
    print('Starting Trading Function. Hour: ' + str(hour) + ' Minute: ' + str(minute))
    if hour == 8 and minute >= 15 and minute <= 17:
        bucketCount = len(tradingStocks)
        print('Trading Bucket Size : ' + str(bucketCount))
        if bucketCount > 0:
            capitalOutlayPounds = 50000
            investmentPounds = capitalOutlayPounds / bucketCount
            print('Investment Per Bucket Item : ' + str(investmentPounds))
            for stock in tradingStocks:
                pricePence = tradingStocks[stock]
                print('Executing : ' + stock + ' @ price ' + str(pricePence))
                units = investmentPounds / (pricePence / 100)
                units = math.floor(units)

                traded[stock + ':' + str(pricePence)] = units
                print('EXECUTED : purchased ' + str(units) + ' units of ' + stock)
    else:
        print('Outside of bAlgo Trading Hours!')
    print('Ending Trading Function')