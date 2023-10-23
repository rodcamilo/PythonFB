#escopo de variável local e global
#local acessível apenas na função
#global acessível no pgm todo
def funcao_local():
    mensagem = "Este é um Escopo LOCAL!"
    print(mensagem)
funcao_local()
