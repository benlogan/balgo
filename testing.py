import analysis_early
import trading
import utilities
import scraper
import sendmail

pricesForAnalysis = {"BIG": [10, 40],
              "VOD": [1.1, 1.2, 1.3],
              "POP": [1.1, 1.1, 1.3],
              "PIP": [1.1, 1.2, 1.2],
              "BAR": [2.2, 2.2, 2.2],
              "NOK": [3.3, 3.1, 3.0]}

testTradingStocks = {"BIG": 110.4, "VOD": 12.5}

testTradedStocks = {"BIG:110.4": 1000}

# TEST FUNCTIONS

#scraper.scrape()
#utilities.printPrices(scraper.prices)

#analysis_early.analysisAverageRising(pricesForAnalysis)
#utilities.printPriceSpot(analysis_early.tradingStocks)

#trading.trade(8, 15, testTradingStocks)

#for trade in trading.traded:
#    print(trade + ' ' + str(trading.traded[trade]) + ' units')

#sendmail.sendMail(trading.traded)

sendmail.sendMail(testTradedStocks)