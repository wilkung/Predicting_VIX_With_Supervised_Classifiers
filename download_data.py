#gold, gold volatility
#yield, yield volatility
#twitter volume of spx, and individual components tweets vs. avg of last 3 mos
#fed speakers
#small cap, large cap
#growth, value
#libor-fedfunds (actual vs. expected)

#actual vol of minutely data for 500 stocks from last x days 
#and figure out dispersion of it like is it everly dispersed 
#(ie. >50% showed uptick in vol or concentrated ie. 20 stocks with 
#very high uptick in minutely vol?)

#find influencers in twitter that spread their opinions

#transformations:
#%chg
#level
#%chg*level
#distance from 1mo mean
#mvg avg
#volume* %chg in spx

#Still, market fear gauges remain contained. 
#The gap between three-month Libor and expected fed-funds rates, 
#for example, stands around 0.08 percentage point, 
#a historically low level. At the height of the financial crisis, 
#that gap was as wide as 4.80 percentage points.

#weather
#http://nipunbatra.github.io/2015/05/weather/
#FX dollar vs. basket
#inflation projects from TIPS
#30y mtg rate
#S&P trading volume
#bad international news
#ensemble of best predictors on twitter based on accuracy of sentiment so top 5 tweeters whose sentiment best predicts movement
#suggested trade
#why use ensemble - why not just use the best one
#how to capture fear in market coming from global geopolitics events?
#daily lda on most popular new articles, find top topics and calculate sentiment of each of the top topics and see the trend of the sentiment of top topics
#or calc sentiment of top googled news words
#libor -

#1. lda on news articles.  get top words in top 5 topics
#2. cross check to see if they were top words googled
#3. if top words persist over time then it is really on people's minds during that period (ie. greece)
#4. if yes, get sentiment over time of top words in topics using that word wih hashtag
#5. combine sentiment of top words of topics and average over them to get sentiment of topic

# code to parse meeting dates of http://pastie.org/2566958

import pandas as pd
from pandas.io.data import DataReader
from datetime import datetime
#
#goog = DataReader('GOOG',  'yahoo', datetime(2010,1,1), datetime(2012,1,1))
#print(goog['Adj Close'])
symbols_list = ['^IRX','^GSPC', '^TNX', '^TYX', 'OIL', 'GLD', '^FVX', '^VIX']
d = {}
for ticker in symbols_list:
    d[ticker] = DataReader(ticker, "yahoo", '2015-01-01')
pan = pd.Panel(d)
df_Adj_Close = pan.minor_xs('Adj Close')
print(df_Adj_Close)
df_Volume = pan.minor_xs('Volume')
print(df_Volume)