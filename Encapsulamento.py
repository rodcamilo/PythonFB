class MinhaClasse:
    def __init__(self):
        self._protegido = 10
        self.__privado = 20
    def _metodo_protegido(self):
        print("Este é um método protegido.")
    def __metodo_privado(self):
        print("Este é um método privado.")
objeto = MinhaClasse()
print(objeto._protegido)
#print(objeto.__privado)
objeto._metodo_protegido()
#objeto.__metodo_privado()
