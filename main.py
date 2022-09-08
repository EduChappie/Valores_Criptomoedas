import requests
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('screen.kv')

class MyApp(App):
    def build(self):
        return GUI
    
    def on_start(self):
        moeda = ["USD", "BTC", "EUR"]

        for x in range(len(moeda)):
            valor = self.getCot(moeda[x])
            self.root.ids[f"moeda{x+1}"].text = f"{moeda[x]} = R$ {valor}"



    # Função para pegar a cotação da moeda
    def getCot(self, moeda):
        link = f"http://economia.awesomeapi.com.br/json/last/{moeda}-BRL" # está pegando o endereço que vai se conectar

        requisicao = requests.get(link) # usou biblioteca requests para pegar a informação do site

        doc_req = requisicao.json() # adicionou .json para o python entender a informação

        return doc_req[f"{moeda}BRL"]["bid"] # e retornou o valor especifico pedido


MyApp().run()