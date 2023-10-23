#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Jogos Olímpicos
# Nome: Cícero Pizzol Libardi
# RA: 168810 
#####################################################

def main():
    # Leitura da primeira linha
    N, O, P, B = [int(x) for x in input().split()]

    # Leitura e processamento das provas

    lista_esportes = []
    dict_paises_pontuacao = dict()
    dict_esportes_ouro = dict()

    for i in range(N):
        esporte, pais_ouro, pais_prata, pais_bronze = [str(x) for x in input().split()]
        lista_esportes.append(esporte)
        
        if pais_ouro not in dict_paises_pontuacao:
            dict_paises_pontuacao[pais_ouro] = O
        else:
            dict_paises_pontuacao[pais_ouro] += O
        dict_esportes_ouro[esporte] = pais_ouro

        if pais_prata not in dict_paises_pontuacao:
            dict_paises_pontuacao[pais_prata] = P
        else:
            dict_paises_pontuacao[pais_prata] += P

        if pais_bronze not in dict_paises_pontuacao:
            dict_paises_pontuacao[pais_bronze] = B
        else:
            dict_paises_pontuacao[pais_bronze] += B

    # Impressão da saída

    pontuacao_max = max(dict_paises_pontuacao.values())
    paises_empatados = []

    for pais in dict_paises_pontuacao.keys():
        if dict_paises_pontuacao[pais] == pontuacao_max:
            paises_empatados.append(pais)

    paises_empatados.sort()

    for pais in paises_empatados:
        print(f"{pais} {pontuacao_max}")
        for esporte in lista_esportes:
            if dict_esportes_ouro[esporte] == pais:
                print(esporte)

main()