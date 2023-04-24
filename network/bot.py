import time

from main import Parsing,CyberParsing
import requests
from bs4 import BeautifulSoup
import telebot

while True:
    Parsing().bundesliga()
    Parsing().division()
    Parsing().MLS()
    CyberParsing().FifaChampionsLeague()
    CyberParsing().syperliga5x5()
    time.sleep(60)


