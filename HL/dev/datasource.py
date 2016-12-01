#%matplotlib inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
from matplotlib.dates import date2num
import pandas as pd
#import pandas_datareader as pd_reader
import pandas_datareader.data as web
import datetime


start = datetime.datetime(2016, 11, 1)
today = end = datetime.datetime.today()

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

class stockdata:
    def __init__(self):
        self.data = None
        self.figure = None
        self.html_output = None
        self.data_df = None
        pass

    def request(self,ticker):
        #res = None #1 query pandas datareader
        res = web.DataReader(ticker, 'yahoo', start, end)
        if len(res) == 0:
            raise SystemExit
        res['Time'] = res.index
        self.data_df = res
        res['Time'] = res['Time'].map(date2num)
        self.data = res[['Time','Open','High','Low','Close']]

    def output(self):
         #2 convert yahoo finance data into printable html format
        #change self.data
        self.html_output = self.data.to_html()
        return self.html_output

    def generate_graph(self):
        plt.clf()
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        #ax.xaxis.set_minor_formatter(dayFormatter)

        #plot_day_summary(ax, quotes, ticksize=3)
        candlestick_ohlc(ax, [tuple(x) for x in self.data.values], width=0.6)

        ax.xaxis_date()
        ax.autoscale_view()

        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

        #plt.show()

        plt.savefig("/Users/linguzhong/Documents/UChicago/Homework/Final/HL/dev/static/dev/stock.png")



import tweepy
class twitterdata:
        def __init__(self):
            self.filters = [{'up':'up','up_credit':0.1,'down':'down','down_credit':-0.1},
                            {'up':'rise','up_credit':0.1,'down':'decline','down_credit':-0.1},
                            {'up':'ascend','up_credit':0.1,'down':'descend','down_credit':-0.1},
                            {'up':'long','up_credit':0.5,'down':'short','down_credit':-0.5},
                            {'up':'buy','up_credit':0.5,'down':'sell','down_credit':-0.5},
                            {'up':'surge','up_credit':1,'down':'slump','down_credit':-1},
                            {'up':'gain','up_credit':0.1,'down':'slip','down_credit':-0.1},
                            {'up':'soar','up_credit':0.8,'down':'tumble','down_credit':-0.8},
                            {'up':'climb','up_credit':0.1,'down':'retreat','down_credit':-0.1},
                            {'up':'rally','up_credit':0.1,'down':'fall','down_credit':-0.1},
                            {'up':'bullish','up_credit':0.1,'down':'bearish','down_credit':-0.1},
                            {'up':'inflow','up_credit':0.1,'down':'outflow','down_credit':-0.1},
                            {'up':'return','up_credit':0.1,'down':'lose','down_credit':-0.5},
                            {'up':'like','up_credit':0.5,'down':'dislike','down_credit':-0.5},
                            {'up':'amazing','up_credit':0.5,'down':'horrible','down_credit':-0.5},
                            {'up':'great','up_credit':0.5,'down':'suck','down_credit':-0.5},
                            {'up':'increase','up_credit':0.1,'down':'decrease','down_credit':-0.1}]
            self.data = None
            self.html_output = None
            self.ckey="8sL9ygWUu8ODwi0J3J3ZtcUBj"
            self.csecret="woffV9hpwlMevwP2oBd9bQBGtTwCNoWtrXmEHX7jmFsOsRER1t"
            self.atoken="4847241653-SlUmHLoo7V9U9nTPQUTESU10jQvP9ffMENzqTie"
            self.asecret="Wk15axb71ncTdijF916I0WaJtdkqV35Rl1l6ZFCcGbsPB"

            self.auth = tweepy.OAuthHandler(self.ckey, self.csecret)
            self.auth.set_access_token(self.atoken, self.asecret)

            self.api = tweepy.API(self.auth)
            self.cur_ticker = None
            self.sentiment = 0

        def request(self,ticker,max_tweets=100):
            query = "$"+ticker
                #1 query twitter api search function
            res = [status.text for status in tweepy.Cursor(self.api.search, q=query).items(max_tweets)]
                #print(res[0:5])
            self.cur_ticker = ticker
            self.data = res

        def process_twits(self):
            score_1 = 0 # analyse self.data and generate our sentiment score.
            score_2 = 0
            score_3 = 0
            for each in self.data:
                    #print (dir(each))
                for each_key_pair in self.filters:

                    if each.find(each_key_pair['up']) != -1:
                        #score += each_key_pair['up_credit']
                            #print('-=-=-=-=-=UP-=-=-=-=-=-=')
                            #print(each)
                        score_1 += 50
                    elif each.find(each_key_pair['down']) != -1:
                            #print('-=-=-=-=-=DOWN-=-=-=-=-=-=')
                            #print(each)
                        #score -= each_key_pair['down_credit']
                        score_2 += 50
                    else:
                        score_3 += 1

            self.sentiment = (score_1,score_2,score_3)
            col_list = ['positive','nagetive','neutral']
            self.data_df = pd.DataFrame([self.sentiment],columns=col_list,index=[self.cur_ticker])
            return self.sentiment

        def generate_graph(self):
            # Example data
            plt.clf()
            plt.rcdefaults()
            sentiment = ('Buy', 'Sell', 'Hold')# maybe other names
            y_pos = np.arange(len(sentiment))
            performance = self.sentiment
            error = np.zeros(len(sentiment))
            #xerr=error
            plt.barh(y_pos, performance, xerr=error, align='center',alpha=0.4)
            plt.yticks(y_pos, sentiment)
            plt.xlabel('Performance')
            plt.title('Twitter sentiment')
            #plt.show()

            plt.savefig("/Users/linguzhong/Documents/UChicago/Homework/Final/HL/dev/static/dev/stock.png")


        def output(self):
            format_func = print #2 convert twitter data into printable html format
            self.html_output = format_func(self.sentiment)
            return self.html_output
