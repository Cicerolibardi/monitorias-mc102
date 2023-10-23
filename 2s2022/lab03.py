###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

# leitura de dados


dia = int(input())
hora = int(input())
minuto = int(input())
estudante = input()
metodo = input()

# valor do ingresso inteiro

dias_da_semana_diurno = [30, 15, 15, 15, 20, 20, 30]
dias_da_semana_noturno = [30, 20, 20, 30, 30, 40, 40]
descontos_diurno = [0.7, 0.5, 0.5, 0.5, 0.5, 0.5, 0.8]
descontos_noturno = [0.7, 0.5, 0.5, 0.5, 0.5, 0.7, 0.8]

# valor a pagar

if hora < 19:
    if hora == 18 and minuto > 30:
        if estudante == "S":
            ingresso = dias_da_semana_noturno[dia - 1] * 0.5
        elif metodo == "C":
            ingresso = dias_da_semana_noturno[dia - 1] * descontos_noturno[dia - 1]
        else:
            ingresso = dias_da_semana_noturno[dia - 1]
    else:
        if estudante == "S":
            ingresso = dias_da_semana_diurno[dia - 1] * 0.5
        elif metodo == "C":
            ingresso = dias_da_semana_diurno[dia - 1] * descontos_diurno[dia - 1]
        else:
            ingresso = dias_da_semana_diurno[dia - 1]   
else:
    if estudante == "S":
        ingresso = dias_da_semana_noturno[dia - 1] * 0.5
    elif metodo == "C":
        ingresso = dias_da_semana_noturno[dia - 1] * descontos_noturno[dia - 1]
    else:
        ingresso = dias_da_semana_noturno[dia - 1]

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))