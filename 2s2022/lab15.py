###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Caça-Palavras
# Nome: Cícero Pizzol Libardi 
# RA: 168810
###################################################


'''
Dada uma matriz, a posição (x,y) e uma sequência
de caracteres, verifica se é possível encontrar 
a palavra
'''
def caca_palavras(matriz, linha, coluna, palavra, pos_palavra, visitado, matriz_transposta):
    encontrou = 0
    if pos_palavra == len(palavra):
        return 1

    for j in range(len(matriz[0])):
        if matriz[linha][j] == palavra[pos_palavra]:
            encontrou = caca_palavras(matriz, linha, j, palavra, pos_palavra + 1, visitado, matriz_transposta)
            if encontrou:
                return encontrou

    for i in range(len(matriz)):
        if matriz_transposta[coluna][i] == palavra[pos_palavra]:
            encontrou = caca_palavras(matriz, i, coluna, palavra, pos_palavra + 1, visitado, matriz_transposta)
            if encontrou:
                return encontrou

    return encontrou

def main():
    matriz = []
    palavras = []

    while True:
        entrada = input()
        if entrada == '0':
            break
        matriz.append(entrada)

    while True:
        entrada = input()
        if entrada == '0':
            break
        palavras.append(entrada)


    matriz_cacar = []
    matriz_transposta = []
    for i in range(len(matriz[0])):
        linha = [0] * len(matriz)
        matriz_transposta.append(linha)


    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[0])):
            linha.append(matriz[i][j])
            matriz_transposta[j][i] = matriz[i][j]

        matriz_cacar.append(linha)

    for palavra in palavras:
        matriz_visitado = [[0 for j in range(len(matriz_cacar[i]))] for i in range(len(matriz_cacar))]
        achou = 0
        for i in range(len(matriz_cacar)):
            for j in range(len(matriz_cacar[0])):
                if matriz_cacar[i][j] == palavra[0]:
                    achou = caca_palavras(matriz_cacar, i, j, palavra, 1, matriz_visitado, matriz_transposta)
                    if achou:
                        break
            if achou:
                break

        if achou:
            print(f"Palavra {palavra}: encontrada")
        else:
            print(f"Palavra {palavra}: nao encontrada")

main()


