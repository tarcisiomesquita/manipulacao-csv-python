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
    
def buscar_PIB(ano, pais):
    rotulos, dados = extrair_dados("Maiores Economias do Mundo (PIB em trilhões de US$ - 2013-2020).csv")
    paises = []
    for i in range(len(dados)):
        paises.append(dados[i][0])
        
    if pais not in paises:
        return "País não disponível."
    elif ano not in rotulos:
        return "Ano não disponível."
    
    indice_ano = rotulos.index(ano)
    indice_pais = paises.index(pais)
    pib = dados[indice_pais][indice_ano]
    
    return f"PIB {pais} em {ano}: US$ {pib} trilhões."

pais = input("Informe um país: ")
ano = input("Informe um ano entre 2013 e 2020: ")
print(buscar_PIB(ano, pais))

    