from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import ttk


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

	info_text['text'] = ""
	parag = ""

	# print screen das informações
	for y in range(len(url)):
		valor = page[y]['cod']

		if 'google' in url[y]:
			parag += "\n{}: {}".format(page[y]['nameCoin'], valor.find_all('div')[385].string)
			print(f"{page[y]['nameCoin']}: R${valor.find_all('div')[385].string}")

		elif page[y]['nameCoin'] == 'Dogecoin':
			parag += "\n{}: {}".format(page[y]['nameCoin'], valor.find_all('span')[42].string)
			print(f"{page[y]['nameCoin']}: {valor.find_all('span')[42].string}")

		else:
			parag += "\n{}: {}".format(page[y]['nameCoin'], valor.find_all('span')[42].div.div.string)
			print(f"{page[y]['nameCoin']}: {valor.find_all('span')[42].div.div.string}")
			pass
	info_text['text'] = parag
	button_verif['text'] = "Atualizar Valor"

	pass

	# Parte Gráfica
window = Tk() # Início
window['padx'] = 70
window['pady'] = 20
window.title("Valores Criptomoedas - eduardofabricio.")

	# Criação Texto do Cabeçalho
h1_text = ttk.Label(window, text="Valor da cotação das Moedas:")
h1_text.grid(column=0, row=0)
h1_text.grid_configure(padx=5, pady=5)
	
	# Criação do Botão
button_verif = ttk.Button(window, text="Verificar Valor", command=cotacao)
button_verif.grid(column=0, row=1)
button_verif.grid_configure(padx=5, pady=5)

info_text = ttk.Label(window, text="")
info_text.grid(column=0, row=2)

window.columnconfigure(0, weight=10)

	# Fim
window.mainloop()
