#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Linha do Tempo Sagrada
# Nome: Cícero Pizzol Libardi
# RA: 168810
#####################################################


def main():

    # Leitura da matriz

    matriz = []
    for i in range(11):
        matriz.append(list(input()))

    # Deteção dos eventos nexus

    for j in range(50):
        executou = True
        coluna_iteracao = j
        linha = 5

        if (matriz[linha+1][j] == "+" or matriz[linha-1][j] == "+"):
            while True:
                if (linha == 0 or linha == 10 or coluna_iteracao == 49 or coluna_iteracao == 0):
                    print(f"Bifurcacao {j}: Evento Nexus")
                    break
                if not executou:
                    print(f"Bifurcacao {j}: Instavel")
                    break

                executou = True
                if linha >= 0 or linha <= 10:
                    if (matriz[linha - 1][coluna_iteracao] == "+"):
                        linha -= 1
                        executou = True
                        matriz[linha][coluna_iteracao] = "."
                        continue
                    if (matriz[linha + 1][coluna_iteracao] == "+"):
                        linha += 1
                        executou = True
                        matriz[linha][coluna_iteracao] = "."
                        continue
                if coluna_iteracao >= 1 or coluna_iteracao <= 48:
                    if (matriz[linha][coluna_iteracao - 1] == "+"):
                        coluna_iteracao -= 1
                        executou = True
                        matriz[linha][coluna_iteracao] = "."
                        continue
                    if (matriz[linha][coluna_iteracao + 1] == "+"):
                        coluna_iteracao += 1
                        executou = True
                        matriz[linha][coluna_iteracao] = "."
                        continue
                executou = False

main()