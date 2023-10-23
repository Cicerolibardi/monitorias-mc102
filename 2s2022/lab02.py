###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Cícero Pizzol Libardi
# RA: 168810
###################################################

# Leitura de dados

d1 = int(input())
v1 = int(input())
t = int(input())
d2 = int(input())
v2 = int(input())

t1 = (d1 / v1) / 24
t2 = (d2 / v2) / 24

if t1 > (t2 + t):
    print("False")
else:
    print("True")
