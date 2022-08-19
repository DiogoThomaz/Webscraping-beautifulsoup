from bs4 import BeautifulSoup
import requests
import re

#cabecalho para emular que a requisao esta sendo feita pelo navegador
cabecalho = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' }


#armazenando resposta do serividor
resposta = requests.get('https://www.magazinevoce.com.br/magazinediogomoreno/celulares-e-smartphones/l/28/', headers=cabecalho)

#transformando a resposta em texto
sopao_macarronico = resposta.text

#deixando a resposta formatada
sopa_bonita = BeautifulSoup(sopao_macarronico, 'html.parser')

#buscando o elemento na resposta
lista_produtos = sopa_bonita.find_all('h3',{'class':re.compile('g-title')})
#empresa = lista_produtos[0].text

#exibindo todos os elementos da lista
for produto in lista_produtos:
    str_produto = produto.contents[0].text
    print(str_produto)

#print(empresa)
#exibindo o tamanho da lista de produtos
print(len(lista_produtos))


lista_precos = sopa_bonita.find_all('p', {'class':'g-price'})

for preco in lista_precos:
    #convertendo cada elemento da lista em uma string separada
    str_preco = preco.contents[0].text
    print(str_preco)



