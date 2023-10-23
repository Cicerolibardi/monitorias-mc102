###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

def ceil_divide_2(x):
    if (x % 2 == 0):
        return int(x/2)
    else:
        return int((x+1)/2)

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def expansao(imagem_original):
    imagem_copia = []
    for i in range(len(imagem_original*2) - 1):
        imagem_appendar = [0] * (len(imagem_original[0])*2 - 1)
        imagem_copia.append(imagem_appendar)

    for i in range(len(imagem_original)):
        for j in range(len(imagem_original[0])):
            i_linha = 2*i
            j_linha = 2*j
            imagem_copia[i_linha][j_linha] = imagem_original[i][j]
            
    
    for i in range(len(imagem_copia)):
        for j in range(len(imagem_copia[0])):
            if (j != 0) and (j != len(imagem_copia[0]) - 1):
                if (i % 2 == 0) and (j % 2 == 1):
                    imagem_copia[i][j] = int((imagem_copia[i][j-1] + imagem_copia[i][j+1]) / 2)
            if (i != 0) and (i != len(imagem_copia) - 1): 
                if (i % 2 == 1) and (j % 2 == 0):
                    imagem_copia[i][j] = int((imagem_copia[i+1][j] + imagem_copia[i-1][j]) / 2)
            if ((i != 0) and (i != len(imagem_copia) - 1) and (j != 0) and (j != len(imagem_copia[0]) - 1)):
                if (i % 2 == 1) and (j % 2 == 1):
                    imagem_copia[i][j] = int((imagem_copia[i-1][j-1] + imagem_copia[i+1][j+1] +
                                            imagem_copia[i-1][j+1] + imagem_copia[i+1][j-1]) / 4)


    return imagem_copia

def retracao(imagem_original):

    linha = ceil_divide_2(len(imagem_original))
    coluna = ceil_divide_2(len(imagem_original[0]))

    i_linha = 0
    j_linha = 0

    imagem_retraida = []
    for i in range(linha):
        imagem_retraida.append([0] * coluna)

    for i in range(0, len(imagem_original), 2):
        j_linha = 0
        for j in range(0, len(imagem_original[0]), 2):
            if (j + 1 < len(imagem_original[0]) and i + 1 < len(imagem_original)):
                valor = int((imagem_original[i][j] + imagem_original[i+1][j] + 
                             imagem_original[i][j+1] + imagem_original[i+1][j+1]) / 4)
                imagem_retraida[i_linha][j_linha] = valor
                j_linha += 1
        i_linha += 1

    if (len(imagem_original[0]) % 2 == 1):
        for i in range(0, len(imagem_original), 2):
            if (i + 1 < len(imagem_original)):
                valor = int((imagem_original[i][len(imagem_original[0]) - 1] + imagem_original[i+1][len(imagem_original[0]) - 1]) / 2)
                imagem_retraida[int(i/2)][coluna - 1] = valor

    if (len(imagem_original) % 2 == 1):
        for i in range(0, len(imagem_original[0]), 2):
            if (i + 1 < len(imagem_original[0])):
                valor = int((imagem_original[len(imagem_original) - 1][i] + imagem_original[len(imagem_original) - 1][i+1]) / 2)
                imagem_retraida[linha - 1][int(i/2)] = valor

    if (len(imagem_original) % 2 == 1) and (len(imagem_original[0]) % 2 == 1):
        imagem_retraida[linha - 1][coluna - 1] = imagem_original[len(imagem_original) - 1][len(imagem_original[0]) - 1]

    return imagem_retraida
    
# leitura da imagem
P2 = input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]

blabla = input() #255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura do tipo de redimensionamento
tipo_entrada = input()

imagem = []
# impressão da imagem final
if tipo_entrada == "retracao":
    imagem = retracao(imagem_original)
else:
    imagem = expansao(imagem_original)

imprimir_imagem(imagem)
