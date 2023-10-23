def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Impossível dividir por 0!"
def obter_numero():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Insira um número válido!")
def obter_operacao():
    while True:
        operacao = input("Digite + ou - ou * ou /: ")
        if operacao in ['+', '-', '*', '/']:
            return operacao
        else:
            print("Operação inválida, digite + ou - ou * ou /")
def calculadora():
    print("Bem-vindo à Calculadora!")
    while True:
        numero1 = obter_numero()
        operacao = obter_operacao()
        numero2 = obter_numero()
        if operacao == '+':
            resultado = adicao(numero1, numero2)
        elif operacao == '-':
            resultado = subtracao(numero1, numero2)
        elif operacao == '*':
            resultado = multiplicacao(numero1, numero2)
        else:
            resultado = divisao(numero1, numero2)
        print("Resultado:", resultado)
        continuar = input("Deseja continuar? Digite S ou N): ")
        if continuar.lower() != 's':
            break
calculadora()