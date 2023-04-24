import random

import requests
from bs4 import BeautifulSoup
class DataMixin:
    def user_context(self,**kwargs):
        context=kwargs
        return context




class Quote:
    def search(self):
        url=requests.get('https://www.azquotes.com/top_quotes.html')
        soup=BeautifulSoup(url.text,'lxml')
        quotes=soup.find_all('a',class_='title')
        quote=random.choice(quotes)
        author=quote.find_next('div',class_='author')
        return f"{quote.text}\n{author.text}"

