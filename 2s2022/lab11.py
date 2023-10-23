#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome: Cícero Pizzol Libardi
# RA: 168810
#####################################################


'''
Dica: A criação das seguintes funções pode facilitar o desenvolvimento
do laboratório:
1- Uma função para rotacionar a peça em 90 graus para direita.
2- Uma função para verificar se é possível encaixar a peça a partir de
uma determinada linha e coluna do tabuleiro.
'''

def rotacao_90(peca):
    peca_rotacionada = []
    for _ in range(len(peca[0])):
        peca_rotacionada.append([])

    for i in range(len(peca)):
        for j in range(len(peca[i])):
            peca_rotacionada[j].insert(0, peca[i][j])
    return peca_rotacionada

def verificar_existencia(tabuleiro, peca):
    ocorrencias = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            quebrou = 0
            for k in range(len(peca)):
                if quebrou == 1:
                    break
                for l in range(len(peca[0])):
                    if i+k < len(tabuleiro) and j+l < len(tabuleiro[0]):
                        if (tabuleiro[i+k][j+l] == "X") and (peca[k][l] == "X"):
                            quebrou = 1
                            break
                    else:
                        quebrou = 1
                        break
            
            if quebrou == 0:
                ocorrencias += 1
    
    return ocorrencias
            

# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())

# Processamento

ocorrencia_normal = verificar_existencia(tabuleiro, peca)
peca = rotacao_90(peca)
ocorrencia_90 = verificar_existencia(tabuleiro, peca)
peca = rotacao_90(peca)
ocorrencia_180 = verificar_existencia(tabuleiro, peca)
peca = rotacao_90(peca)
ocorrencia_270 = verificar_existencia(tabuleiro, peca)

# Impressão do resultado

print(f"{ocorrencia_normal},{ocorrencia_90},{ocorrencia_180},{ocorrencia_270}")
