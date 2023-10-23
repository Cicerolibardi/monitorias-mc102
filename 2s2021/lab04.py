###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

def incrementar_elementos(incremento, elemento_principal, elemento_oposto):
    elemento_principal += incremento
    elemento_oposto -= incremento / 2
    if elemento_oposto < 0:
        elemento_oposto = 0

    return elemento_principal, elemento_oposto


def main():
    # Inicialização das variáveis
    water = 0
    earth = 0
    fire = 0
    air = 0

    # Leitura da sequência de treinamento
    while True:
        elemento_str = input()
        if elemento_str == "W":
            elemento_val = int(input())
            water, fire = incrementar_elementos(elemento_val, water, fire)
        elif elemento_str == "F":
            elemento_val = int(input())
            fire, water = incrementar_elementos(elemento_val, fire, water)
        elif elemento_str == "E":
            elemento_val = int(input())
            earth, air = incrementar_elementos(elemento_val, earth, air)
        elif elemento_str == "A":
            elemento_val = int(input())
            air, earth = incrementar_elementos(elemento_val, air, earth)
        elif elemento_str == "X":
            break

    # Impressão das informações de saída

    print("Pontuacao Final")
    print("Agua: {:.1f}".format(water))
    print("Terra: {:.1f}".format(earth))
    print("Fogo: {:.1f}".format(fire))
    print("Ar: {:.1f}".format(air))

    if ((water > 0) and (fire > 0) and (earth > 0) and (air > 0)):
        print("Treinamento realizado com sucesso.")
    else:
        print("Realize mais treinamentos.")

main()