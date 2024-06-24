from alpha_vantage.timeseries import TimeSeries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
import codecs
class Api:
    def __init__(self, stock_symbol = "AAPL"):
        with open("Alpha_Vantage_API_Key.txt") as file:
            API_KEY = file.read()
        self.API_KEY = API_KEY.strip()
        self.stock_symbol = stock_symbol
        self.time_series = TimeSeries(key = self.API_KEY, output_format = "pandas")
    def __str__(self):
        return f"Working with apla vantange API {self.API_KEY}"

    def get_stats(self, criteria = "month"):
        if criteria == "week":
            dataframe, metastore = self.time_series.get_weekly(self.stock_symbol)
        elif criteria == "day":
            dataframe, metastore = self.time_series.get_intraday(self.stock_symbol)
        else:
            dataframe, metastore = self.time_series.get_monthly(self.stock_symbol)
            
        self.data = pd.DataFrame(dataframe).transpose().reset_index()
        print(self.data)
    def request_stats(self, criteria = "month", csv = False):
        if criteria == "week":
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+str(self.stock_symbol)+'&apikey='+str(self.API_KEY)
        elif criteria == "day":
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+str(self.stock_symbol)+'&apikey='+str(self.API_KEY)
        else:
            url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+str(self.stock_symbol)+'&apikey='+str(self.API_KEY)
        
        
        if csv:
            r = requests.get(url + '&datatype=csv').content
            self.data = pd.read_csv(io.StringIO(r.decode("utf-8")))
            self.data.transpose().reset_index()
        else:
            r = requests.get(url)
            self.data = BeautifulSoup(r.content)
        print(self.data)

        

        
apple = Api()
print(apple)
apple.get_stats(criteria = "week")
# print(apple.get_stats(criteria = "day"))
# print(apple.get_stats())
apple.request_stats(criteria = "day", csv = True)