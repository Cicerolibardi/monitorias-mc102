##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Cícero Pizzol Libardi
# RA: 168810
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]

torre_ordenada = sorted(torre)
# Leitura e processamento dos movimentos
while True:
    nova_torre = []
    posicao = int(input())
    if posicao == 0:
        break
    for i in range(posicao):
        nova_torre.append(torre[i])
    nova_torre = nova_torre[::-1]

    torre[:posicao] = nova_torre[:posicao]

    
for i in range(len(torre)):
    certo = True
    if torre_ordenada[i] != torre[i]:
        certo = False
        break

if certo:
    print("Torre estavel")
else:
    print("Torre instavel")

# Impressão da saída
