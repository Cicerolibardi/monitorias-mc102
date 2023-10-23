#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Cícero Pizzol Libardi
# RA: 168810
#####################################################

# Leitura da matriz

n = int(input())
matriz = [input().split() for _ in range(n)]

# Leitura e processamento dos caminhos

time_inicial = input()

time_a_jogar = 0
if time_inicial != "azul":
    time_a_jogar = 1

qtd_jogadores = int(input())


pontos_vermelho = 0
pontos_azul = 0

for i in range(qtd_jogadores):
    caminho_percorrido = input()
    posX = 0
    posY = 0
    for j in range(len(caminho_percorrido)):
        if caminho_percorrido[j] == "N":
            posX -= 1
        elif caminho_percorrido[j] == "S":
            posX += 1
        elif caminho_percorrido[j] == "L":
            posY += 1
        elif caminho_percorrido[j] == "O":
            posY -= 1

        if matriz[posX][posY] == "*":
            matriz[posX][posY] = '.'
            if time_a_jogar % 2 == 0:
                pontos_azul += 1
            else:
                pontos_vermelho += 1
    
    time_a_jogar += 1
            
# Impressão da saída

print(f"Tesouros encontrados pelo time azul: {pontos_azul}")
print(f"Tesouros encontrados pelo time vermelho: {pontos_vermelho}")

if pontos_azul > pontos_vermelho:
    print("Vitoria do time azul")
elif pontos_vermelho > pontos_azul:
    print("Vitoria do time vermelho")
else:
    print("Empate")


