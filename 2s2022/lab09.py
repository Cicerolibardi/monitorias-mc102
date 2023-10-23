###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

# Leitura de dados

def leitura(entrada):
    entrada = entrada.split(":")

    for i in range(len(entrada)):
        entrada[i] = list(entrada[i])
    entrada[0].pop()
    entrada[1].remove(" ")

    for i in range(len(entrada)):
        entrada[i] = "".join(entrada[i])
    entrada[1] = int(entrada[1])

    return entrada



estoque = {}
# Processamento
while True:
    entrada = input()
    if entrada == "FIM":
        break

    entrada = leitura(entrada)

    if entrada[0] in estoque:
        if entrada[1] < 0:
            if (estoque[entrada[0]][0] + entrada[1]) < 0:
                print("Quantidade indisponivel para a venda de " + str(entrada[1] * -1) + " unidade(s) do produto " + entrada[0] + ".")
            else:
                estoque[entrada[0]][0] += entrada[1]
                estoque[entrada[0]][2] += 1
        else:
            estoque[entrada[0]][0] += entrada[1]
            estoque[entrada[0]][1] += 1
    else:
        if entrada[1] < 0:
            print("Quantidade indisponivel para a venda de " + str(entrada[1] * -1) + " unidade(s) do produto " + entrada[0] + ".")
        else:
            estoque[entrada[0]] = [entrada[1], 1, 0]


    # Impressão da saída
lista_produtos_ordenados = sorted(estoque.keys())

for elemento in lista_produtos_ordenados:
    print("Produto: " + elemento)
    print("Quantidade em Estoque: " + str(estoque[elemento][0]))
    print("Pedidos de Compra: " + str(estoque[elemento][1]))
    print("Pedidos de Venda: " + str(estoque[elemento][2]))

