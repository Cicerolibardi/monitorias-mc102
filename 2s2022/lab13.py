###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

# Leitura de dados

votos = dict()

entrada = input()   

while True:
    if entrada == "0":
        break
    
    if entrada not in votos:
        votos[entrada] = 0

    votos[entrada] += 1

    entrada = input()


lista_votos_ordenados = sorted(votos.keys())
lista_votos_ordenados = lista_votos_ordenados[::-1]

maior = 0
elemento_maior = ""
while True:
    maior = 0
    if len(votos) > 2:
        for elemento in votos:
            if votos[elemento] > maior and elemento != "Branco" and elemento != "Nulo":
                maior = votos[elemento]
                elemento_maior = elemento
    else:
        break

    print(f"{elemento_maior} {maior}")
    votos.pop(elemento_maior)

elemento = "Branco"
print(f"Brancos {votos[elemento]}")
elemento = "Nulo"
print(f"Nulos {votos[elemento]}")


# Saída de dados