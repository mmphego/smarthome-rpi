import urllib
try:
    from html.parser import HTMLParser
except:
    from HTMLParser import HTMLParser

class QuoteData:
    pass

class GoogleFinanceParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.quote = QuoteData()
        self.quote.price = -1

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            last_itemprop = ""
            for attr, value in attrs:
                if attr == "itemprop":
                    last_itemprop = value

                if attr == "content" and last_itemprop == "name":
                    self.quote.name = value
                if attr == "content" and last_itemprop == "price":
                    self.quote.price = value
                if attr == "content" and last_itemprop == "priceCurrency":
                    self.quote.priceCurrency = value
                if attr == "content" and last_itemprop == "priceChange":
                    self.quote.priceChange = value
                if attr == "content" and last_itemprop == "priceChangePercent":
                    self.quote.priceChangePercent = value
                if attr == "content" and last_itemprop == "quoteTime":
                    self.quote.quoteTime = value
                if attr == "content" and last_itemprop == "exchange":
                    self.quote.exchange = value
                if attr == "content" and last_itemprop == "exchangeTimezone":
                    self.quote.exchangeTimezone = value


def getquote(symbol):
    url = "http://finance.google.com/finance?q=%s" % symbol
    content = urllib.urlopen(url).read()

    gfp = GoogleFinanceParser()
    gfp.feed(content)
    return gfp.quote;


quote = getquote('CSCO')
print quote.name, quote.price
