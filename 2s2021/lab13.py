###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

# Dada uma sequência de números de inteiros, gera
# uma string representando a pilha de panquecas
def str_panquecas(lista):
    return(" ".join(map(str, lista)))

def sort_panquecas(lista_panquecas):
    ultima_pos = len(lista_panquecas)
    executou = False
    while True:
        i_max = 0
        valor_maximo = lista_panquecas[0]

        for i in range(ultima_pos):
            if (lista_panquecas[i] > valor_maximo):
                i_max = i
                valor_maximo = lista_panquecas[i]
        
        if (i_max != ultima_pos - 1):
            print(f"Posicionando a panqueca {valor_maximo}")

            lista_aux = lista_panquecas[:i_max+1]
            for i in range(i_max + 1):
                lista_panquecas[i] = lista_aux[i_max-i]

            if (i_max != 0):
                print(f"Primeira inversao: {str_panquecas(lista_panquecas)}")

            lista_aux = lista_panquecas[:ultima_pos]
            for i in range(ultima_pos):
                lista_panquecas[i] = lista_aux[ultima_pos-1-i]
            print(f"Segunda inversao: {str_panquecas(lista_panquecas)}")
            
            executou = True

        ultima_pos -= 1
        if (ultima_pos == 0):
            break
        
    if not executou:
        print("Panquecas ja ordenadas")

def main():
    lista_panquecas = [int(x) for x in input().split()]
    sort_panquecas(lista_panquecas)
main()