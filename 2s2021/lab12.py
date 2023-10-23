###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Processamento de Imagens
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

def flip_horizontal(imagem_original):
    B_flipada = []
    for i in range(len(imagem_original)):
        B_flipada.append(imagem_original[i][::-1])

    return B_flipada

def flip_vertical(imagem_original):
    B_flipada = []
    for i in range(len(imagem_original) - 1, -1, -1):
        B_flipada.append(imagem_original[i])
    return B_flipada

def rotacao_90(imagem_original):
    B_rotacionada = []
    for _ in range(len(imagem_original[0])):
        B_rotacionada.append([])

    for i in range(len(imagem_original)):
        for j in range(len(imagem_original[i])):
            B_rotacionada[j].insert(0, imagem_original[i][j])
    return B_rotacionada
    
def rotacao_180(imagem_original):
    B_rotacionada_90 = rotacao_90(imagem_original)
    B_rotacionada_180 = rotacao_90(B_rotacionada_90)
    return B_rotacionada_180

def verificar_existencia_e_printar(imagem_original, imagem_flip_horizontal, 
                                    imagem_flip_vertical, imagem_rot_90, imagem_rot_180, imagem_pequena):
    original_contida = False
    horizontal_contida = False
    vertical_contida = False
    rot_180_contida = False
    rot_90_contida = False

    for i in range(len(imagem_original)):
        for j in range(len(imagem_original[i])):
            qtd_iguais_original = 0
            qtd_iguais_horizontal = 0
            qtd_iguais_vertical = 0
            qtd_iguais_180 = 0
            qtd_iguais_90 = 0
            for k in range(len(imagem_pequena)):
                quebrou_original = False
                quebrou_horizontal = False
                quebrou_vertical = False
                quebrou_180 = False
                quebrou_loop = False
                for l in range(len(imagem_pequena[k])):
                    if ((i+k < len(imagem_original)) and (j+l < len(imagem_original[i]))):
                        if (imagem_pequena[k][l] != imagem_original[i+k][j+l]):
                            qtd_iguais_original = 0
                            quebrou_original = True
                        else:
                            qtd_iguais_original += 1

                        if (imagem_flip_horizontal[k][l] != imagem_original[i+k][j+l]):
                            qtd_iguais_horizontal = 0
                            quebrou_horizontal = True
                        else:
                            qtd_iguais_horizontal += 1

                        if (imagem_flip_vertical[k][l] != imagem_original[i+k][j+l]):
                            qtd_iguais_vertical = 0
                            quebrou_vertical = True
                        else:
                            qtd_iguais_vertical += 1
                
                        if (imagem_rot_180[k][l] != imagem_original[i+k][j+l]):
                            qtd_iguais_180 = 0
                            quebrou_180 = True
                        else:
                            qtd_iguais_180 += 1
                    else:
                        break

                    if (quebrou_original and quebrou_horizontal and quebrou_vertical and quebrou_180):
                        quebrou_loop = True
                        break
                    
                if quebrou_loop:
                    break
            
            for k in range(len(imagem_rot_90)):
                quebrou_90 = False
                for l in range(len(imagem_rot_90[k])):
                    if (i+k < len(imagem_original) and j+l < len(imagem_original[i])):
                        if (imagem_rot_90[k][l] != imagem_original[i+k][j+l]):
                            qtd_iguais_90 = 0
                            quebrou_90 = True
                        else:
                            qtd_iguais_90 += 1

                        if quebrou_90:
                           break
                    else:
                        break
                if quebrou_90:
                    break

            if (qtd_iguais_original == len(imagem_pequena)*len(imagem_pequena[0])):
                original_contida = True
            if (qtd_iguais_horizontal == len(imagem_flip_horizontal)*len(imagem_flip_horizontal[0])):
                horizontal_contida = True
            if (qtd_iguais_vertical == len(imagem_flip_vertical)*len(imagem_flip_vertical[0])):
                vertical_contida = True
            if (qtd_iguais_180 == len(imagem_rot_180)*len(imagem_rot_180[0])):
                rot_180_contida = True
            if (qtd_iguais_90 == len(imagem_rot_90)*len(imagem_rot_90[0])):
                rot_90_contida = True

    if original_contida:
        print("Original: Contido")
    else:
        print("Original: Nao contido")
    if horizontal_contida:
        print("Flip horizontal: Contido")
    else:
        print("Flip horizontal: Nao contido")
    if vertical_contida:
        print("Flip vertical: Contido")
    else:
        print("Flip vertical: Nao contido")
    if rot_90_contida:
        print("Rotacao 90: Contido")
    else:
        print("Rotacao 90: Nao contido")
    if rot_180_contida:
        print("Rotacao 180: Contido")
    else:
        print("Rotacao 180: Nao contido")

def main():
    # leitura da imagem A
    _ = input() #P2 - linha a ser ignorada

    m_A, n_A = [int(x) for x in input().split()]

    _ = input() #255 - linha a ser ignorada

    A = []
    for i in range(n_A):
        linha = [int(x) for x in input().split()]
        A.append(linha)

    # leitura da imagem A
    _ = input() #P2 - linha a ser ignorada

    m_B, n_B = [int(x) for x in input().split()]

    _ = input() #255 - linha a ser ignorada

    B = []
    for i in range(n_B):
        linha = [int(x) for x in input().split()]
        B.append(linha)

    B_flip_horizontal = flip_horizontal(B)
    B_flip_vertical = flip_vertical(B)
    B_rotacionada_90 = rotacao_90(B)
    B_rotacionada_180 = rotacao_180(B)
    verificar_existencia_e_printar(A, B_flip_horizontal, B_flip_vertical, 
                                    B_rotacionada_90, B_rotacionada_180, B)

main()