###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################


'''
Dada uma matriz e a posição (x,y), realiza a 
verificação de é possível realizar a fuga da cidade
ou se é necessário o resgate aéreo.
'''
def fuga(matriz, matriz_visitado, linha, coluna):

    if (linha < 0 or linha == len(matriz) or coluna < 0 or coluna == len(matriz[0])):
        return True
    else:
        if matriz_visitado[linha][coluna] == 0:
            matriz_visitado[linha][coluna] = 1
            if (matriz[linha][coluna] == "N"):
                return False
            elif (matriz[linha][coluna] == "T"):
                retorno = fuga(matriz, matriz_visitado, linha-1, coluna)
                if retorno == True:
                    return True
                retorno = fuga(matriz, matriz_visitado, linha+1, coluna)
                if retorno == True:
                    return True
                retorno = fuga(matriz, matriz_visitado, linha, coluna-1)
                if retorno == True:
                    return True
                retorno = fuga(matriz, matriz_visitado, linha, coluna+1)
                if retorno == True:
                    return True
            elif (matriz[linha][coluna] == "V"):
                retorno = fuga(matriz, matriz_visitado, linha-1, coluna)
                if retorno == True:
                    return True
                retorno = fuga(matriz, matriz_visitado, linha+1, coluna)
                if retorno == True:
                    return True
            elif (matriz[linha][coluna] == "H"):
                retorno = fuga(matriz, matriz_visitado, linha, coluna-1)
                if retorno == True:
                    return True
                retorno = fuga(matriz, matriz_visitado, linha, coluna+1)
                if retorno == True:
                    return True
    return False


def main():
    # Leitura de dados

    matriz = []    
    while True:
        linha_input = input().split()
        if not linha_input[0].isnumeric():
            matriz.append(linha_input)
        else:
            break
    
    n = int(linha_input[0])
    # Verifica se é preciso realizar a fuga da cidade
    # ou solicitar o resgate aéreo para cada posição
    #   ...]
    for i in range(n):
        linha, coluna = [int(x) for x in input().split()]
        matriz_visitado = [[0 for j in range(len(matriz[i]))] for i in range(len(matriz))]
        retorno = fuga(matriz, matriz_visitado, linha, coluna)
        if retorno:
            print("Fuga da cidade realizada.")
        else:
            print("Resgate aereo solicitado.")
main()