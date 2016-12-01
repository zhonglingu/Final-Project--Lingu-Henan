from django.db import models

# Create your models here.
STOCKS = (
    ('gspc','S&P'),
    ('aapl','Apple'),
    ('tsla','Tesla'),
    ('bac',	'Bank of America'),
    ('c',	'Citigroup'),
    ('f',	'Ford'),
    ('twtr','Twitter'),
    ('fb',	'Facebook'),
    ('bac',	'Bank of America'),

)

STOCKS_DICT = dict(STOCKS)

class Input(models.Model):

    ticker = models.CharField(max_length=50, choices=STOCKS)
    name  = models.CharField(max_length=50)
