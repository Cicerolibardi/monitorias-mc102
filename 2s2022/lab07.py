###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

# Leitura das tropas de defesa

qtd_defesa = int(input())

# Leitura das tropas de ataque
tropas_defesa = []
for i in range(qtd_defesa):
    tropas_defesa.append(int(input()))

qtd_ataque = int(input())

tropas_ataque = []
for i in range(qtd_ataque):
    tropas_ataque.append(int(input()))

posicao = 0
for i in range(qtd_defesa):
    vitoria = 0
    empate = 0
    derrota = 0
    for j in range(qtd_ataque):
        if i + j >= qtd_defesa:
            posicao = -1
            break
        if tropas_defesa[i+j] > tropas_ataque[j]:
            derrota += 1
        elif tropas_defesa[i+j] == tropas_ataque[j]:
            empate += 1
        else:
            vitoria += 1
    
    if posicao == -1:
        break

    if vitoria > derrota:
        posicao = i + 1
        break


# Processamento da guerra


# Saída de dados
if posicao == -1:
    print('Derrota')
else:
    print('Vitória posicionando as tropas a partir da posição', posicao)