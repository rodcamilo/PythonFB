#escopo de variável local e global
#local acessível apenas na função
#global acessível no pgm todo
variavel_global = "Este é um Escopo GLOBAL!"
def funcao_acessa_global():
    print(variavel_global)
funcao_acessa_global()
