import requests
from bs4 import BeautifulSoup
import pandas as pd
symbolCode = '0'
header = {
 "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
   "X-Requested-With": "XMLHttpRequest"
}


# to get list of symbols in the csv file
def fno_list():
    df = pd.read_csv("https://www1.nseindia.com/content/fo/fo_mktlots.csv")
    df = df.drop(df.index[3])
    fno_list_data = df.iloc[:,1].to_list()
    fno_list_data = [x.strip(' ') for x in fno_list_data]
    return fno_list_data


# return the required pandas data frame
def Option_Chain_Scrapper(stock_name):
    a = fno_list().index(stock_name)
    my_url_nse = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=' + stock_name
    page_nse = requests.get(my_url_nse,headers=header)

    df = pd.read_html(page_nse.text)
    # df[1] is the requiired table in the page
    return df[1]
