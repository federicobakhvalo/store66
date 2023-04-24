import requests
import telebot
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json
import time

id='958968720'
bot=telebot.TeleBot('6036042905:AAFfXMYP9yNIi_onUhJRniOi7sxdn3OOCK4')
class Parsing:
    def bundesliga(self):

        try:
            url = requests.get('https://1xstavka.ru/live/football/2055972-budnesliga-lfl-5x5')
            soup = BeautifulSoup(url.text, 'lxml')
            teams = [c.text for c in soup.find_all('span', class_='c-events__teams')]
            teams = [x.replace('\n', ' ') for x in teams]

            goals = [int(r.text) for r in
                     soup.find_all('span', class_='c-events-scoreboard__cell c-events-scoreboard__cell--all')]
            time1 = [r.text for r in soup.find_all('div', class_='c-events__time')][0].split('\n')[1]
            time2 = [r.text for r in soup.find_all('div', class_='c-events__time')][-1].split('\n')[1]
            if (goals[0] + goals[1] >= 3 and int(time1[:2]) <= 6) or (
                    goals[0] + goals[1] >= 4 and int(time1[:2]) <= 10) or (
                    goals[0] + goals[1] >= 5 and int(time1[:2]) <= 14) or (goals[0] + goals[1] >= 6):
                bot.send_message(chat_id=id,text=
                    f"{time1}     {teams[0]}\n\t\t\t\t\t{goals[0]} ============ {goals[1]}\n_____________________________________________")
            if (goals[-2] + goals[-1] >= 3 and int(time2[:2]) <= 6) or (
                    goals[-1] + goals[-2] >= 4 and int(time2[:2]) <= 10) or (
                    goals[-1] + goals[-2] >= 5 and int(time2[:2]) <= 14) or (goals[-1] + goals[-2] >= 6):
                bot.send_message(chat_id=id,text=f"{time2}     {teams[-1]}\n\t\t\t\t\t{goals[-2]} ======= {goals[-1]}\n_____________________________________________________")
        except:
            print('NotYet')

    def division(self):
        try:
            url = requests.get('https://1xstavka.ru/live/football/2055846-division-4h4')
            soup = BeautifulSoup(url.text, 'lxml')
            teams = [str(x) for x in soup.find('span', class_='c-events__teams').text.splitlines() if x != '']
            goals = [int(c.text) for c in
                     soup.find_all('span', class_='c-events-scoreboard__cell c-events-scoreboard__cell--all')]
            time = soup.find('div', class_='c-events__time').find('span').text
            time_for_test = int(time[:2])
            if (sum(goals)>=3 and time_for_test<=7) or (sum(goals)>=2 and time_for_test<=4) or (sum(goals)>=5 and time_for_test<=13) or sum(goals)>=7:
                bot.send_message(chat_id=id,text=f"{time}    {teams[0]}     {teams[1]}\n\t\t\t\t\t{goals[0]} ========= {goals[-1]}")
        except:
            print("niiii")
    def MLS(self):
        try:
            url=requests.get('https://1xstavka.ru/live/football/2183824-mls-5x5')
            soup=BeautifulSoup(url.text,'lxml')
            event1=[str(x) for x in soup.find('span',class_='c-events__teams').text.splitlines() if x!=''][:2]
            event2=[str(x) for x in soup.find('span',class_='c-events__teams').find_next('span',class_='c-events__teams').text.splitlines() if x!=''][:2]
            goals=[int(r.text) for r in soup.find_all('span',class_='c-events-scoreboard__cell c-events-scoreboard__cell--all')]
            timer1=soup.find('div',class_='c-events__time').find('span').text
            def change_timer(timer):
                return int(timer[:2])
            timer_for_test=change_timer(timer1)
            if (goals[0]+goals[1]>=3 and timer_for_test<=7) or (goals[0]+goals[1]>=4 and timer_for_test<=7) or (goals[0]+goals[1]>=5 and timer_for_test<=12) or (goals[0]+goals[1]>=7):
                bot.send_message(chat_id=id,text=f"MLS League {timer1}   {event1[0]}      {event1[-1]}\n\t\t\t\t\t{goals[0]} =========== {goals[1]}")

        except:
            pass









class CyberParsing:

    def FifaChampionsLeague(self):
        try:
            url = requests.get('https://1xbet155642.top/live/fifa/2392595-fifa-22-champions-league')
            soup = BeautifulSoup(url.text, 'lxml')
            match = soup.find('div').find('span', class_='game-scores__num')
            n = ''
            while match.text == '0':
                match = match.find_next('span', class_='game-scores__num')
                n = match
            matches = [r.replace(' ', '') for r in
                       n.find_previous('div',
                                       class_='ui-dashboard-cell dashboard-game-block dashboard-game__block').text.split(
                           '\n') if r != '']
            teams = [str(x) for x in matches if x.isalpha() == True]
            time = matches[-1][:5]
            goals = [int(x) for x in list(matches[4])]
            time_for_test = int(time[:2])
            if (sum(goals) >= 2 and time_for_test <= 25) or (sum(goals) >= 3 and time_for_test <= 45) or sum(
                goals) >= 4:
                bot.send_message(chat_id=id,text=f"Cyber Champions League\n {time_for_test}' {teams[0]}        {teams[-1]}\n\t\t\t{goals[0]} ========= {goals[-1]}")

        except:
            pass
    def syperliga5x5(self):
        try:
            url=requests.get('https://1xbet155642.top/live/fifa/2414089-fifa-22-5x5-superleague')
            soup=BeautifulSoup(url.text,'lxml')
            match=soup.find('div')
            match1=soup.find('div').find_all('span',class_='game-scores__num')
            n=[]
            for i in range(len(match1)):

                if match1[i].text!='0':

                    n.append(match1[i].find_previous('div',class_='ui-dashboard-cell dashboard-game-block dashboard-game__block').text.replace(' ','').splitlines())
            teams=[x for x in n[0] if len(x)!=0]
            goals=[int(x) for x in list(teams[2])]
            time=int(teams[-1][:2])
            if (sum(goals)>=2 and time<=2) or (sum(goals)>=3 and time<=3) or sum(goals)>=4:
                bot.send_message(chat_id=id,text=f"Superliga5x5\n{time}'    {teams[0]}   {goals[0]}  :  {teams[1]}     {goals[-1]}")
        except:
            pass























class Parser:
    url = requests.get('https://soccer365.ru/online/&tab=1')
    soup = BeautifulSoup(url.text, 'lxml')
    match = []

    def get(self):
        matches = self.soup.find_all('div', class_='game_block online')
        self.match = [r.text for r in matches]

    def chx(self):
        for i in range(len(self.match)):
            match = self.match[i].splitlines()[2:-8]
            goals = sum([int(x) for x in match if x.isnumeric() == True])
            if match[0] == 'Перерыв':
                time = 45
            else:
                time = int(''.join([str(x) for x in match[0] if x.isnumeric() == True]))
            if (goals >= 4 and time <= 70) or (goals >= 2 and time <= 25) or goals >= 3:
                print(' '.join(match))

x=Parser()
x.get()
x.chx()


