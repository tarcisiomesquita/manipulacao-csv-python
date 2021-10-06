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
    
def listar_variacoes_PIBs():
    rotulos, dados = extrair_dados("Maiores Economias do Mundo (PIB em trilhões de US$ - 2013-2020).csv")

    indice_inicial = rotulos.index("2013")
    indice_final = rotulos.index("2020")
    
    for elemento in dados:
        pais = elemento[0]
        pib_inicial = float(elemento[indice_inicial])
        pib_final = float(elemento[indice_final])
        variacao = (pib_final / pib_inicial - 1) * 100
        print(f"{'{0:<20}'.format(pais)} Variação de {round(variacao, 2)}% entre 2013 e 2020.")

listar_variacoes_PIBs()