from django.shortcuts import render
from django.http import HttpResponse
from .datasource import stockdata,twitterdata
# Create your views here.
def index(request):
    return HttpResponse("Hi everyone.Henan and Lingu are going to present their project to you")

from os.path import join
from django.conf import settings
import sqlite3, pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from .forms import InputForm
from .models import STOCKS_DICT

def stockinfo(request, stock = None):
    # stock data
    stock = request.GET.get('stock', '')
    if not stock: stock = request.POST.get('stock', 'gspc')

    #if stock:
    #    df = df[df["stock"].str.lower() == stock.lower()]
    stk = stockdata()
    stk.request(stock)
    stk.generate_graph()
    df = stk.data_df
    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    params = {'form_action' : reverse_lazy('dev:stockinfo'),
                'form_method' : 'get',
                'form' : InputForm({'stock' : stock}),
                'stock' : STOCKS_DICT[stock],
                'html_table': table,

                'pic_source': join('/static/', 'dev/stock.png')}
                #'pic_source': reverse_lazy('dev:pic', kwargs = {'stock': stock})}

    return render(request, 'stockinfo.html', params)

import matplotlib
matplotlib.style.use('ggplot')

def homepage(request):

    return render(request, 'homepage.html')


def form(request, stock = None):
    #twitter
    stock = request.GET.get('stock', '')
    if not stock: stock = request.POST.get('stock', 'aapl')

    #if stock:
    #    df = df[df["stock"].str.lower() == stock.lower()]
    twtr = twitterdata()
    twtr.request(stock)
    twtr.process_twits()
    twtr.generate_graph()
    df = twtr.data_df
    table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.
    del twtr

    params = {'form_action' : reverse_lazy('dev:form'),
                'form_method' : 'get',
                'form' : InputForm({'stock' : stock}),
                'stock' : STOCKS_DICT[stock],
                'html_table': table,

                'pic_source': join('/static/', 'dev/stock.png')}
                #'pic_source': reverse_lazy('dev:pic', kwargs = {'stock': stock})}

    return render(request, 'form.html', params)
