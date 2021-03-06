#test.py
from yahoo_finance import Share
from alpha_vantage.timeseries import TimeSeries
from newsapi import NewsApiClient
from pytrends.request import TrendReq

import matplotlib.pyplot as plt
from IPython.display import display

"""
google trends data
"""
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["walmart stock"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='GLOBAL', gprop='')

interest_over_time_df = pytrends.interest_over_time()
print(interest_over_time_df)

"""
price data
"""
ts = TimeSeries(key='G9V53KVNRI8KMSXH', output_format='pandas')
wmt_price, meta_data = ts.get_daily(symbol='WMT', outputsize='full') #get all historic prices
print(wmt_price)
wmt_price['4. close'].plot()
plt.title('Walmart ')


"""
news data
"""
newsapi = NewsApiClient(api_key='ff0f41a5f9804ed69aa4e250e0ae9177')
news_data = newsapi.get_everything(q='walmart',
                                    sources='bloomberg, cnn, nbc-news, the-washington-post, the-wall-street-journal, politico',
                                    from_param='2020-05-01',
                                    to='2020-05-27',
                                    language='en',
                                    page_size=100)

#get sources
#print(newsapi.get_sources())

#print(news_data.keys())
#print(news_data.items())
#print(news_data['totalResults'])


variable_name = news_data['articles']
#print(len(variable_name))
# for i in range(news_data['totalResults']):
#print(variable_name[0])

for i in range(len(variable_name)):
    title = variable_name[i]
    print(title['title'])


plt.show()
#data, meta_data = ts.get_daily(symbol='JNUG')
#print(data)
#data['4. close'].plot()
#plt.title('JNUG')
#plt.show()
