import requests
from bs4 import BeautifulSoup
import time
import datetime

# hardcoded FTSE250 list
stocks = ["3IN", "FOUR", "888", "ASL", "AGK", "AAF", "AJB", "ATST", "ATT", "ACI", "AO.", "APAX", "ASCL", "ASHM", "AGR", "AML", "AGT", "AVON", "BAB", "BGFD", "BGS", "USA", "BBY", "BNKR", "BBH", "BBGI", "BEZ", "BWY", "BIFF", "BYG", "BRSC", "BRWM", "BCPT", "BGSC", "BOY", "BRW", "BVIC", "CCR", "CNE", "CLDN", "CLSN", "CPI", "CAPC", "CCL", "CEY", "CNA", "CHG", "CINE", "CTY", "CSH", "CKN", "CBG", "CLI", "CMCX", "COA", "CCC", "GLO", "CTEC", "CSP", "CWK", "CRST", "DPH", "DLN", "DPLM", "DLG", "DGOC", "DC.", "DOM", "DRX", "DNLM", "EZJ", "EDIN", "EWI", "ECM", "ELM", "ENOG", "ESNT", "ERM", "JEO", "FCIT", "FDM", "FXPO", "FCSS", "FEV", "FSV", "FGT", "FGP", "FSFL", "FRAS", "FUTR", "GFS", "GAW", "GYS", "GCP", "DIGS", "GSS", "GNS", "GFTU", "GRI", "GPOR", "UKW", "GNC", "GRG", "HMSO", "HVPE", "HAS", "HTWS", "HSL", "HRI", "HGT"]
prices = {}

tradingStocks = {}

scrapeInterval = 2  # scraping interval (mins)

URL = 'https://www.hl.co.uk/shares/stock-market-summary/ftse-250'
# public site, streaming prices only when authenticated

# actual scraping function
def scrape():
    try:
        print("SCRAPE STARTING : " + URL)
        page = requests.get(URL)
    except requests.exceptions.RequestException as e:
        print("PAGE REQUEST ERROR", e)
        #https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/
        #add custom timeout and retry later
        return #but continue, i.e. try again next time

    print("SCRAPE PROCESSING STARTED")
    #print(page)

    soup = BeautifulSoup(page.content, 'html.parser')

    #row = soup.find(id='ls-row-3IN-L')
    #print(results.prettify())

    #price = soup.find(id='ls-mid-3IN-L')
    #print(price.text)

    priceTime = datetime.datetime.now()
    print(priceTime)
    for stock in stocks:
        price = soup.find(id='ls-mid-' + stock + '-L')
        price = price.text.replace(",", "") # strip comma
        #prices[stock] = price.text

        if stock in prices:
            prices[stock].append(price)
        else:
            prices[stock] = [price]

        #result = stock + ' price : ' + price.text
        #print(result)

# debug/print
def printPrices(pricesForPrinting):
    for stock in pricesForPrinting:
        print(stock)
        historicalPrices = pricesForPrinting[stock]
        for historicalPrice in historicalPrices:
            print(historicalPrice)

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

# look for stocks that are trending up over a period of time
# or just look for an average price rise of a certain size and only run/monitor during the opening 30 minutes
def analysisAverageRising(pricesForAnalysis):
    tradingStocks = {}
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

                if percentageRise > 1:
                    print('LARGE PERCENTAGE RISE : ' + stock + " is UP " + str(percentageRise) + "%")
                    tradingStocks[stock] = latestPrice
                    print('PRICE HISTORY...')
                    for historicalPrice in historicalPrices:
                        print(historicalPrice)
    print("Ending Data Analysis")

def trade(tradingStocks):
    time = datetime.datetime.now()
    if time.hour >= 8 and time.minute >= 15:
    #if time.hour >= 22 and time.minute >= 0:
        print('TRADING! ' + str(time))
        bucketCount = len(tradingStocks)
        print('BUCKET COUNT : ' + str(bucketCount))
        if bucketCount > 0:
            capitalOutlayPounds = 50000
            investmentPounds = capitalOutlayPounds / bucketCount
            print('INVESTMENT PER STOCK : ' + str(investmentPounds))
            for stock in tradingStocks:
                print('EXECUTING : ' + stock + ' @ ' + str(tradingStocks[stock]))
                pricePence = tradingStocks[stock]
                units = investmentPounds / (pricePence / 100)
                print('PURCHASED ' + str(units) + ' UNITS OF ' + stock)


def start():
    scrape()
    printPrices(prices)
    analysisAverageRising(prices)
    trade(tradingStocks)

    #time.sleep(5)
    # sleep for 15 minutes, to allow a price refresh
    time.sleep(60 * scrapeInterval)

while True:
    start()


"""
testPrices = {"BIG": [10, 40],
              "VOD": [1.1, 1.2, 1.3],
              "POP": [1.1, 1.1, 1.3],
              "PIP": [1.1, 1.2, 1.2],
              "BAR": [2.2, 2.2, 2.2],
              "NOK": [3.3, 3.1, 3.0]}
analysisAverageRising(testPrices)

testTradingStocks = {"BIG": 110.4, "VOD": 12.5}
trade(testTradingStocks)
"""

