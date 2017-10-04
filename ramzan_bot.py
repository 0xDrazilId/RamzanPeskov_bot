import configramzan
import telebot
import random
from bs4 import BeautifulSoup
import urllib.request
bot = telebot.TeleBot(configramzan.token)


@bot.message_handler(commands=['traffic'])
def get_traffic(message):
	html = urllib.request.urlopen("http://yandex.ru")
	soup = BeautifulSoup(html, 'lxml')
	icon_traf = soup.find('a', {'href' : 'https://yandex.ru/maps/51/samara/probki', 'class':'link link_black_yes'}).next_element.get('class')
	res_traf = soup.find('a', {'href': 'https://yandex.ru/maps/51/samara/probki', 'class': 'link link_black_yes'}).next_element.next_element
	if (icon_traf[2] == "b-ico-traffic-gn"):
		icontrf = "✅"
		comment = "Спасибо, мистер Азаров"
		bot.send_message(message.chat.id, "Яндекс говорит, что пробки в Самаре сейчас:\n" + icontrf + " " + res_traf + "\n" + comment + "\n\nНу сам посмотри: https://yandex.ru/maps/51/samara/probki")
	if (icon_traf[2] == "b-ico-traffic-yw"):
		icontrf = "⚠️"
		comment = "Пробки средненькие"
		bot.send_message(message.chat.id, "Яндекс говорит, что пробки в Самаре сейчас:\n" + icontrf + " " + res_traf + "\n" + comment + "\n\nНу сам посмотри: https://yandex.ru/maps/51/samara/probki")
	if (icon_traf[2] == "b-ico-traffic-rd"):
		icontrf = "🛑"
		comment = "Вы держитесь здесь. Вам счастливой дороги!"
		bot.send_message(message.chat.id, "Яндекс говорит, что пробки в Самаре сейчас:\n" + icontrf + " " + res_traf + "\n" + comment + "\n\nНу сам посмотри: https://yandex.ru/maps/51/samara/probki")

@bot.message_handler(commands=['news'])
def get_news(message):
	news = ""
	html = urllib.request.urlopen("http://yandex.ru")
	soup = BeautifulSoup(html, 'lxml')
	all_the_news = soup.find_all('a', class_='home-link list__item-content home-link_black_yes')
	for c in all_the_news:
		if c.find_parent('div', class_ = 'content-tabs__items content-tabs__items_active_true'):
			news_title = "📌" + c.get('aria-label')
			news_link = c.get('href')
			news = news + news_title + "\n" + news_link + "\n\n"				
	bot.send_message(message.chat.id, news)

@bot.message_handler(commands=['samara'])
def get_news(message):
	news = ""
	html = urllib.request.urlopen("http://yandex.ru")
	soup = BeautifulSoup(html, 'lxml')
	all_the_news = soup.find_all('a', class_='home-link list__item-content home-link_black_yes')
	for c in all_the_news:
		if c.find_parent('div', class_ = 'content-tabs__items content-tabs__items_active_false'):
			news_title = "📌" + c.get('aria-label')
			news_link = c.get('href')
			news = news + news_title + "\n" + news_link + "\n\n"			
	bot.send_message(message.chat.id, news)


@bot.message_handler(commands=['weather'])
def get_weather(message):
	html = urllib.request.urlopen("https://www.gismeteo.ru/city/daily/4618")
	soup = BeautifulSoup(html, 'lxml')
	temperat = soup.find('a', class_='home-link home-link_black_yes').get('aria-label')
	bot.send_message(message.chat.id, temperat)

if __name__ == '__main__':
	bot.polling(none_stop=True)
