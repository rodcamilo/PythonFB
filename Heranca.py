class Forma:
    def __init__(self, cor):
        self.cor = cor
    def calcular_area(self):
        pass
class Retangulo(Forma):
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
    def calcular_area(self):
        return self.largura * self.altura
import math
class Circulo(Forma):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio
    def calcular_area(self):
        return math.pi * self.raio ** 2
retangulo = Retangulo("Azul", 5, 4)
circulo = Circulo("Vermelho", 3)
print(f"Área do retângulo: {retangulo.calcular_area()}")
print(f"Área do círculo: {circulo.calcular_area()}")
