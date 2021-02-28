import requests
from bs4 import BeautifulSoup
import datetime

URL = 'https://www.hl.co.uk/shares/stock-market-summary/ftse-250'
# public site, streaming prices only when authenticated

# hardcoded FTSE250 list
stocks = ["3IN", "FOUR", "888", "ASL", "AGK", "AAF", "AJB", "ATST", "ATT", "ACI", "AO.", "APAX", "ASCL", "ASHM", "AGR", "AML", "AGT", "AVON", "BAB", "BGFD", "BGS", "USA", "BBY", "BNKR", "BBH", "BBGI", "BEZ", "BWY", "BIFF", "BYG", "BRSC", "BRWM", "BCPT", "BGSC", "BOY", "BRW", "BVIC", "CCR", "CNE", "CLDN", "CLSN", "CPI", "CAPC", "CCL", "CEY", "CNA", "CHG", "CINE", "CTY", "CSH", "CKN", "CBG", "CLI", "CMCX", "COA", "CCC", "GLO", "CTEC", "CSP", "CWK", "CRST", "DPH", "DLN", "DPLM", "DLG", "DGOC", "DC.", "DOM", "DRX", "DNLM", "EZJ", "EDIN", "EWI", "ECM", "ELM", "ENOG", "ESNT", "ERM", "JEO", "FCIT", "FDM", "FXPO", "FCSS", "FEV", "FSV", "FGT", "FGP", "FSFL", "FRAS", "FUTR", "GFS", "GAW", "GYS", "GCP", "DIGS", "GSS", "GNS", "GFTU", "GRI", "GPOR", "UKW", "GNC", "GRG", "HMSO", "HVPE", "HAS", "HTWS", "HSL", "HRI", "HGT"]

# scraped prices dict
prices = {}

# actual scraping function
def scrape():
    print('Starting Scrape : ' + URL)
    try:
        page = requests.get(URL)
    except requests.exceptions.RequestException as e:
        print("PAGE REQUEST ERROR", e)
        #https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/
        #add custom timeout and retry later
        return #but continue, i.e. try again next time

    #print(page)

    soup = BeautifulSoup(page.content, 'html.parser')

    #row = soup.find(id='ls-row-3IN-L')
    #print(results.prettify())

    #price = soup.find(id='ls-mid-3IN-L')
    #print(price.text)

    #priceTime = datetime.datetime.now()
    #print(priceTime)
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
    print('Ending Scrape')