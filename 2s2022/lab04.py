###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

# leitura da sequência de compras e vendas
num_entrada = int(input())
acumulado = 0
qtd_vendas = 0
while num_entrada != 0:
    if num_entrada < 0:
        if acumulado + num_entrada < 0:
            print(f"Quantidade indisponível para a venda de {num_entrada * -1} unidades.")
        else:
            acumulado += num_entrada
            qtd_vendas += 1
    else:
        acumulado += num_entrada
    num_entrada = int(input())

print(f"Quantidade de vendas realizadas: {qtd_vendas}")
print(f"Quantidade em estoque: {acumulado}")

# impressão da saída
