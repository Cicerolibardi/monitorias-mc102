###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

def main():
    # Leitura de dados
    t = int(input())
    dist_a = int(input())
    vel_a = float(input())
    t_pit_stop = float(input())
    dist_b = int(input())
    vel_b = float(input())

    # Convertendo de Km/h para m/s
    vel_a = vel_a / 3.6
    vel_b = vel_b / 3.6

    # Cálculo do tempo total gasto para realizar o pit stop
    t_tot_boxes = (dist_a / vel_a) + (dist_b / vel_b) + t_pit_stop

    # Impressão da resposta
    if (t_tot_boxes < t):
        print("True")
    else:
        print("False")

main()