#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome: Cícero Pizzol Libardi
# RA: 168810
#####################################################

"""
Esta função recebe como parâmetro uma matriz que representa o tabuleiro,
uma posição atual (linha_atual, coluna_atual) no tabuleiro, uma posição 
final (linha_fim, coluna_fim) desejada e o parâmetro cor indica a cor da
última posição visitada no caminho.
O retorno esperado para a função é um valor booleano, com True indicando 
que foi possível encontrar um caminho e False indicando que não existe um
caminho.
"""

def caminho(tabuleiro, linha_atual, coluna_atual, linha_fim, coluna_fim, cor, tabuleiro_visitado):
    encontrou = 0
    tabuleiro_visitado[linha_atual][coluna_atual] = "v"


    if (linha_atual == linha_fim and coluna_atual == coluna_fim):
        return 1

    if (linha_atual > 0):
        cor_prox = tabuleiro[linha_atual - 1][coluna_atual]
        if (cor != cor_prox and tabuleiro_visitado[linha_atual - 1][coluna_atual] == "a"):
            encontrou = caminho(tabuleiro, linha_atual - 1, coluna_atual, linha_fim, coluna_fim, cor_prox, tabuleiro_visitado)
            if (encontrou == 1):
                return encontrou

    if (linha_atual < (len(tabuleiro) - 1)):
        cor_prox = tabuleiro[linha_atual + 1][coluna_atual]
        if (cor != cor_prox and tabuleiro_visitado[linha_atual + 1][coluna_atual] == "a"):
            encontrou = caminho(tabuleiro, linha_atual + 1, coluna_atual, linha_fim, coluna_fim, cor_prox, tabuleiro_visitado)
            if (encontrou == 1):
                return encontrou

    if (coluna_atual > 0):
        cor_prox = tabuleiro[linha_atual][coluna_atual - 1]
        if (cor != cor_prox and tabuleiro_visitado[linha_atual][coluna_atual - 1] == "a"):
            encontrou = caminho(tabuleiro, linha_atual, coluna_atual - 1, linha_fim, coluna_fim, cor_prox, tabuleiro_visitado)
            if (encontrou == 1):
                return encontrou

    if (coluna_atual < len(tabuleiro[0]) - 1):
        cor_prox = tabuleiro[linha_atual][coluna_atual + 1]
        if (cor != cor_prox and tabuleiro_visitado[linha_atual][coluna_atual + 1] == "a"):
            encontrou = caminho(tabuleiro, linha_atual, coluna_atual + 1, linha_fim, coluna_fim, cor_prox, tabuleiro_visitado)
            if (encontrou == 1):
                return encontrou

    return encontrou

# Leitura dos dados

tamanho = int(input())
tabuleiro = [input().split() for _ in range(tamanho)]
l1, c1, l2, c2 = [int(i) for i in input().split()]
tabuleiro_visitado = []
for i in range(len(tabuleiro)):
    tabuleiro_visitado.append(["a"] * len(tabuleiro[0]))

# Verificação se existe um caminho

encontrou = caminho(tabuleiro, l1, c1, l2, c2, tabuleiro[l1][c1], tabuleiro_visitado)
if encontrou == 1:
    print("caminho encontrado")
else:
    print("caminho nao encontrado")
