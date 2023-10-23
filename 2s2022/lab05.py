##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Cícero Pizzol Libardi
# RA: 168810
##################################################

# Leitura do valor da hora
from subprocess import HIGH_PRIORITY_CLASS


V = int(input())

# Leitura do numero de dias trabalhados na semana
D = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia
hora_extra = 0
tempo_trabalho = 0
for i in range(D):
    tempo_trabalho_parcial = 0
    qtd_turnos = int(input())
    for j in range(qtd_turnos):
        inicio = int(input())
        fim = int(input())
        tempo_trabalho += fim - inicio
        tempo_trabalho_parcial += fim - inicio
    if tempo_trabalho_parcial > 8:
        hora_extra += tempo_trabalho_parcial - 8

# Calculo do valor devido ao funcionário
valor =  V * tempo_trabalho
if hora_extra > 0:
    valor += V/2 * hora_extra


if tempo_trabalho - hora_extra > 44:
    valor += V/2 * (tempo_trabalho - hora_extra - 44)

if tempo_trabalho > 44 and (tempo_trabalho - hora_extra) > 44:
    hora_extra = tempo_trabalho - 44

# Impressão da saída
print("Horas trabalhadas:", tempo_trabalho)
print("Horas extras:", hora_extra)
print("Valor devido: R$ {:0.2f}".format(valor))
