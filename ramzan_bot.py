import config
import telebot
import random
from bs4 import BeautifulSoup
import urllib.request

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['traffic'])
def get_traffic(message):
	html = urllib.request.urlopen("http://yandex.ru")
	soup = BeautifulSoup(html, 'lxml')
	res_traf = soup.find('i', class_ = 'b-ico traffic__icon b-ico-traffic-yw').next_element
	if (res_traf.find_parent('li').get(class_)=="b-ico traffic__icon b-ico-traffic-gn"):
		icon_traf = "✅"
		comment = "Спасибо, мистер Азаров"
	if (res_traf.find_parent('li').get(class_)=="b-ico traffic__icon b-ico-traffic-yw"):
		icon_traf = "⚠️"
		comment = "Пробки средненькие"
	if (res_traf.find_parent('li').get(class_)=="b-ico traffic__icon b-ico-traffic-rd"):
		icon_traf = "🛑"
		comment = "Вы держитесь здесь. Вам счастливой дороги!"
	bot.send_message(message.chat.id, "Яндекс говорит, что пробки в Самаре сейчас:\n" + icon_traf + " " + res_traf + "\nНу сам посмотри: https://yandex.ru/maps/51/samara/probki")

@bot.message_handler(commands=['news'])
def get_news(message):
	html = urllib.request.urlopen("http://yandex.ru")
	soup = BeautifulSoup(html, 'lxml')
	all_the_news = soup.find_all('a', class_='home-link list__item-content home-link_black_yes')
	for c in all_the_news:
		if c.find_parent('div', class_ = 'content-tabs__items content-tabs__items_active_true'):
			news_title = c.get('aria-label')
			news_link = c.get('href')
			bot.send_message(message.chat.id, news_title + "\n" + news_link + "\n\n")

@bot.message_handler(commands=['samara'])
def get_news(message):
	html = urllib.request.urlopen("http://yandex.ru")
	soup = BeautifulSoup(html, 'lxml')
	all_the_news = soup.find_all('a', class_='home-link list__item-content home-link_black_yes')
	for c in all_the_news:
		if c.find_parent('div', class_ = 'content-tabs__items content-tabs__items_active_false'):
			news_title = c.get('aria-label')
			news_link = c.get('href')
			bot.send_message(message.chat.id, news_title + "\n" + news_link + "\n\n")
    #a = random.randint(0, 101)
    #bot.send_message(message.chat.id, a)


if __name__ == '__main__':
	bot.polling(none_stop=True)
