#definição
meu_array = [10, 20, 30, 40, 50, 10]
print("Elementos:", meu_array)
#modificação
meu_array[5] = 60
print("Sexto elemento corrigido:", meu_array)
#inclusão
meu_array.append(70)
print("Sétimo elemento incluído:", meu_array)
#exclusão
meu_array.pop(0)
print("Primeiro elemento excluído:")
for elemento in meu_array:
    print(elemento)
