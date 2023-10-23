###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

def main():
    # Leitura da matriz
    # DICA: o método isnumeric() pode ser útil para determinar o fim da leitura da matriz 
    matriz_mapa = []
    while True:
        linha_input = input().split()
        if not linha_input[0].isnumeric():
            matriz_mapa.append(linha_input)
        else:
            break
    
    qtd_iteracoes = int(linha_input[0])
    linha = 0
    coluna = 0

    # Leitura das coordenadas, início do processamento e impressão da saída
    matriz_visitado = []
    for i in range(qtd_iteracoes):
        matriz_visitado = [[0 for j in range(len(matriz_mapa[i]))] for i in range(len(matriz_mapa))]
        linha, coluna = [int(i) for i in input().split()]
        while True:
            matriz_visitado[linha][coluna] = 1
            
            if (matriz_mapa[linha][coluna] == "N"):
                linha -= 1
                if (linha < 0):
                    print("Fuga pelo norte.")
                    break

            elif (matriz_mapa[linha][coluna] == "S"):
                linha += 1
                if (linha == len(matriz_mapa)):
                    print("Fuga pelo sul.")
                    break

            elif (matriz_mapa[linha][coluna] == "L"):
                coluna += 1
                if (coluna == len(matriz_mapa[0])):
                    print("Fuga pelo leste.")
                    break

            elif (matriz_mapa[linha][coluna] == "O"):
                coluna -= 1
                if (coluna < 0):
                    print("Fuga pelo oeste.")
                    break
            
            if (matriz_visitado[linha][coluna] == 1):
                print("Resgate aereo solicitado.")
                break

main()