from alpha_vantage.timeseries import TimeSeries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
import codecs

with open("Alpha_Vantage_API_Key.txt") as file:
    API_KEY = file.read()
API_KEY = API_KEY.strip()

ts1 = TimeSeries(key = API_KEY)
print(ts1.get_monthly("AAPL"))

print(ts1.get_weekly("AAPL"))

print(ts1.get_daily("AAPL"))