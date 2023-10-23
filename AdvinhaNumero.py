import random
n_aleatorio = random.randint(1,10)
tentativas=0
while True:
    n_usuario = int(input("Digite um número de 1 a 10: "))
    tentativas+=1
    if n_usuario == n_aleatorio:
        print(f"Parabéns, você acertou em {tentativas} tentativas")
        break
    elif n_usuario > n_aleatorio:
        print("Digite um número menor")
    elif n_usuario < n_aleatorio:
        print("Digite um número maior")
