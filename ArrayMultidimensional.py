#definição de arrya dentro de array
matriz = [[0, 1, 2],[3, 4, 55],[6, 7, 8]]
#acessando
print("Primeiro elemento da primeira matriz:", matriz[0][0])
print("Segundo elemento da primeira matriz:", matriz[0][1])
print("Terceiro elemento da primeira matriz:", matriz[0][2])
print("Primeiro elemento da segunda matriz:", matriz[1][0])
print("Segundo elemento da segunda matriz:", matriz[1][1])
print("Terceiro elemento da segunda matriz:", matriz[1][2])
print("Primeiro elemento da terceira matriz:", matriz[2][0])
print("Segundo elemento da terceira matriz:", matriz[2][1])
print("Terceiro elemento da terceira matriz:", matriz[2][2])
#modificando
matriz[1][2]=5
print("Correção:", matriz)
#iterando
print("Elementos da matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
