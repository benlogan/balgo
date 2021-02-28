import time
import datetime
from sendmail import sendMail
from utilities import printPrices
import scraper
import analysis_early
import trading

scrapeInterval = 2  # scraping interval (mins)

def start():
    timeNow = datetime.datetime.now()
    today = datetime.datetime.today().weekday() # monday = 0

    if today <= 4 and (timeNow.hour >= 8 and timeNow.hour < 17):
    #if timeNow:
        print('Executing bAlgo Pipeline. Market Hours. Time : ' + str(timeNow))

        scraper.scrape()
        #printPrices(scraper.prices)

        analysis_early.analysisAverageRising(scraper.prices)

        trading.trade(timeNow.hour, timeNow.minute, analysis_early.tradingStocks)

        if len(trading.traded) > 0:
            sendMail(trading.traded)
    else:
        print('Market Closed! ' + str(timeNow))

    # sleep for X minutes, to allow a price refresh
    time.sleep(60 * scrapeInterval)

while True:
    start()