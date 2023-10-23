###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Cícero Pizzol Libardi 
# RA: 168810
###################################################

# Leitura da palavra
palavra = input()

palavra_copia = ''
for elemento in palavra:
    palavra_copia += elemento

# Leitura dos palpites e impressão do resultado para cada palpite

correto = False
for i in range(6):
    tentativa = input()
    palavra_para_printar = ''
    for i in range(len(tentativa)):
        if tentativa[i] not in palavra:
            palavra_para_printar += "_"
        elif tentativa[i] == palavra_copia[i]:
            palavra_para_printar += tentativa[i].upper()
            tentativa = list(tentativa)
            tentativa[i] = '.'
            tentativa = "".join(tentativa)
        elif tentativa[i] in palavra_copia:
            palavra_para_printar += tentativa[i]
    
    print(palavra_para_printar)
    if palavra_para_printar.lower() == palavra:
        correto = True
        break

# Impressão da linha final
if correto:
    print("Resposta correta")
else:
    print("Palavra correta:", palavra)