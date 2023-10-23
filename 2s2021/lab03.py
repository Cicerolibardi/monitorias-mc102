###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cartões de Crédito
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

def main():
    # Leitura de dados
    score = int(input())
    idade = int(input())
    saldo = float(input())
    salario = float(input())

    # Verificação se o cartão de crédito será concedido ou não
    concedido = True
    if (score < 300):
        concedido = False

    elif (score >= 300 and score < 600):
        if (idade < 30):
            concedido = False
        else:
            if (salario < 3000.00):
                concedido = False
            else:
                if (saldo < 7000.00):
                    concedido = False

    else:
        if (idade < 50 and salario < 2000.00 and saldo < 5000.00):
            concedido = False

    if (concedido):
        print("Cartao concedido")
    else:
        print("Cartao nao concedido")

main()