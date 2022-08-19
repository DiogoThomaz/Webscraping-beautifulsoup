#biblioteca beautifulsoup para lidar com as html
#biblioteca request para fazer requisicoes a sites
#biblioteca pandas para analise e manipulacao de dados
#biblioteca numpy para trabalhar com os arrays
#biblioteca re (regex) para trabalhar com expressoes regulares

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

#cabecalho para emular que a requisao esta sendo feita pelo navegador
cabecalho = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' }


#fazendo uma requisicao ao servidor e armazenando em uma variavel
#request.get --> faz a requisacao a url (url, dizendo que ha cabecalho)
resposta = requests.get('https://www.magazinevoce.com.br/magazinediogomoreno/celulares-e-smartphones/l/28/',
 headers=cabecalho)

#transformando a requisicao em texto
sopao_macarronico = resposta.text

#deixando a resposta formatada
sopa_bonita = BeautifulSoup(sopao_macarronico, 'html.parser')

#buscando todos elementos h3 com a classe
#usando find_all --> .find_all('elemento', {'class': 'nome da classe'}) 
lista_produtos = sopa_bonita.find_all('h3',{'class':re.compile('g-title')})
lista_precos = sopa_bonita.find_all('p', {'class':'g-price'})

#Cria uma variavel para armazenar as duas listas geradas
lista_zip = []

#Juntando dois for em somente um comando
for produto, preco in zip (lista_produtos, lista_precos):
    

    #produto.contents[posicao inicial].text --> gera lista de produtos
    #replace retira ou troca uma informacao por outra 
    str_produto = produto.contents[0].text.replace(',','').replace('\n', '').replace('.','').replace('"','')
    str_preco = preco.contents[0].text.replace('R$', '').replace('.','').replace(',','.')
    
    # append junta as duas listas geradas em uma unica lista,
    #intercalando as informacoes com uma informacao de str_produto com str_preco
    lista_zip.append((str_produto, str_preco))

#criando um data frame da lista zipada // 
# pd.DataFrame --> gera data frame da lista
# columns --> adicionar cabecalho
df_exibir = pd.DataFrame(lista_zip, columns=['Produto', 'Preco'])
print(df_exibir)


#exportando o dataframe para csv e salvando no computador
#explicacao  --> (lista, sem a virgula do cabecalho)
df_exibir.to_csv('lista.csv', index=False)