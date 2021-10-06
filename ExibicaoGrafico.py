def extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        conteudo = arquivo.read()
        
    conteudo = conteudo.splitlines()
    rotulos = conteudo.pop(0)
    rotulos = rotulos.split(',')
    dados = []
    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)
        
    return rotulos, dados

import matplotlib.pyplot as plt

def exibir_grafico(x, y):
    plt.plot(x, y)
    plt.show()
    
def exibir_graficos_pais_PIB(pais):
    rotulos, dados = extrair_dados("Maiores Economias do Mundo (PIB em trilhões de US$ - 2013-2020).csv")
    
    paises = []
    for i in range(len(dados)):
        paises.append(dados[i][0])
        
    if pais not in paises:
        print("País não disponível.")
        exit()

    lista_anos = rotulos[1:]
    lista_PIBs = [] 
    for elemento in dados:
        if elemento[0] == pais:
            for i in range (1, len(elemento)):
                lista_PIBs.append(float(elemento[i]))
                
    exibir_grafico(lista_anos, lista_PIBs)
    
pais = input("Informe um país: ")
exibir_graficos_pais_PIB(pais)