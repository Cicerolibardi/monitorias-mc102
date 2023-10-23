#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Linha do Tempo Sagrada II
# Nome: Cícero Pizzol Libardi
# RA:
#####################################################


"""
Esta função recebe como parâmetro uma matriz, uma posição inicial 
de uma ramificação na matriz determinada pelos parâmetros linha 
e coluna. O retorno esperado para a função é um número inteiro 
indicando a quantidade de eventos nexus gerados pela ramificação.
"""
def eventos_nexus(matriz, linha, coluna):
    valor_retorno = 0
    if ((linha == 0 or linha == (len(matriz) -1 )or coluna == 0 or coluna == (len(matriz[0]) - 1))):
        if (matriz[linha][coluna] == "+"):  
            matriz[linha][coluna] = "."
            valor_retorno += 1

        return valor_retorno
    else:
        matriz[linha][coluna] = "."
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if ((0 <= (linha+i) < len(matriz)) and (0 <= (coluna+j) < len(matriz[0]))):
                    if (matriz[linha+i][coluna+j] == "+"):
                        valor_retorno += eventos_nexus(matriz, linha+i, coluna+j)

    return valor_retorno

def main():
    # Leitura da matriz

    matriz = []
    for i in range(11):
        matriz.append(list(input()))

    X = 0
    # Deteção dos eventos nexus
    for i in range(len(matriz[0])):
        if (matriz[4][i] == "+"):
            X = eventos_nexus(matriz, 4, i)
            print("Ramificacao {0}: {1} Eventos Nexus.".format(i, X))
        elif (matriz[6][i] == "+"):
            X = eventos_nexus(matriz, 6, i)
            print("Ramificacao {0}: {1} Eventos Nexus.".format(i, X))


main()