from bs4 import BeautifulSoup
import requests

	# 4 moedas sendo verificadas
url = ['https://coinmarketcap.com/pt-br/currencies/ethereum/', 'https://coinmarketcap.com/pt-br/currencies/dogecoin/', 'https://coinmarketcap.com/pt-br/currencies/bitcoin/', 'https://www.google.com/finance/quote/USD-BRL?window=5Y']
moedas = ['Ethereum', 'Dogecoin', 'Bitcoin', 'Dolar$']

def cotacao():
	# função para mostrar a cotação do Bitcoin e do Dolar

	# page = [{'coin_name': 'Bitcoin', 'value': 3 }]
	page = []
	soup = []

	# requerimento dos sites
	for x in range(len(url)):
		soup.append({'info': requests.get(url[x])})
		pass

	# adiçao no array de moedas
	for x in range(len(url)):
		page.append({'nameCoin': moedas[x], 'cod': BeautifulSoup(soup[x]['info'].content, 'html.parser')})
		pass

	# print screen das informações
	for y in range(len(url)):

		valor = page[y]['cod']
		if 'google' in url[y]:
			print(f"{page[y]['nameCoin']}: R${valor.find_all('div')[385].string}")
		elif page[y]['nameCoin'] == 'Dogecoin':
			print(f"{page[y]['nameCoin']}: {valor.find_all('span')[42].string}")
		else:
			print(f"{page[y]['nameCoin']}: {valor.find_all('span')[42].div.div.string}")
			pass

	pass

cotacao()
