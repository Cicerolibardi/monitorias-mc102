###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

def main():
    # Leitura de dados
    sequencia = [int(i) for i in input().split()]
    quebrou = False

    for _ in range(len(sequencia)):
        aux = sequencia[0]
        sequencia.pop(0)
        sequencia.append(aux)

        for i in range(1,len(sequencia)):
            if (sequencia[i-1] > sequencia[i]):
                break
        else:
            print("Klift, Kloft, Still, a porta se abriu")
            quebrou = True
            break
        
    if (not quebrou):
        print("Senha incorreta")
        
main()