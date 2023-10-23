###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Vacinação AstraZeneca
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################


def main():
    # Leitura dos dados

    N = int(input())
    qtd_vacinas_mes = []

    # Listas dos números de vacinados com a primeira e segunda dose em cada mês

    D1 = []
    D2 = []

    # Lista do número de vacinas devolvidas em cada mês

    X = []

    for i in range(N):
        vacinas = int(input())
        qtd_vacinas_mes.append(vacinas)
        D1.append(0)
        D2.append(0)
        X.append(0)

    # Processamento dos dados

    for i in range(N):
        qtd_vacina_atual = qtd_vacinas_mes[i]
        if (i > 2 and i < N - 3):
            if (D1[i-3] > 0):
                D2[i] = min([qtd_vacina_atual, D1[i-3]])
                D1[i] = D2[i] - D1[i-3]
                qtd_vacina_atual -= D1[i-3]
            if (qtd_vacina_atual > 0):
                if (qtd_vacina_atual >= qtd_vacinas_mes[i+3]):
                    D1[i] = min([qtd_vacinas_mes[i+3], qtd_vacina_atual])
                    X[i] = abs(qtd_vacina_atual - qtd_vacinas_mes[i+3])
                else:
                    D1[i] = qtd_vacina_atual
        elif (N <= i + 3):
            if (D1[i-3] > 0):
                D2[i] = min([qtd_vacina_atual, D1[i-3]])
                D1[i] = D2[i] - D1[i-3]
                qtd_vacina_atual -= D1[i-3]
            if (qtd_vacina_atual > 0):
                D1[i] = qtd_vacina_atual
        elif (i <= 2):
            if (i+3 < N):
                D1[i] = min([qtd_vacinas_mes[i+3], qtd_vacina_atual])
                if (qtd_vacina_atual >= qtd_vacinas_mes[i+3]):
                    X[i] = abs(qtd_vacina_atual - qtd_vacinas_mes[i+3])
            else:
                D1[i] = qtd_vacina_atual
    
    # Impressão do uso das vacinas mês a mês
    soma_D1 = 0
    soma_D2 = 0
    soma_X = 0

    for i in range(N):
        print("Mes " + str(i+1) + ":")
        print("Vacinados com a primeira dose:", D1[i])
        print("Vacinados com a segunda dose:", D2[i])
        print("Vacinas devolvidas:", X[i])
        soma_D1 += D1[i]
        soma_D2 += D2[i]
        soma_X += X[i]

    # Impressão do resumo final
    print("Total:")
    print(f"Vacinados apenas com a primeira dose: {abs(soma_D1 - soma_D2)}")
    print(f"Vacinados com as duas doses: {soma_D2}")
    print(f"Vacinas devolvidas: {soma_X}")

main()