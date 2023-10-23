###################################################

# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################



def main():
    # Leitura de dados
    fita_DNA = input()
    primer = input()
    primer = primer[1:-1]
    primer = primer[::-1]

    # Verificação da ligação dos primers na fita
    contador = 0
    idx_ligacoes = []
    for i in range(len(fita_DNA)):
        for j in range(len(primer)):
            if ((fita_DNA[i+j] == "A" and primer[j] == "T") or (fita_DNA[i+j] == "C" and primer[j] == "G") or
                (fita_DNA[i+j] == "G" and primer[j] == "C") or (fita_DNA[i+j] == "T" and primer[j] == "A")):
                contador += 1
            else:
                break
        if (contador == len(primer)):
            idx_ligacoes.append(i)
        contador = 0
        
    # Impressão da saída do programa
    if (len(idx_ligacoes) == 0):
        print("Nenhuma ligacao")
    else:
        for i in range(len(idx_ligacoes)):
            print(f"Ligacao na posicao {idx_ligacoes[i]}")

main()