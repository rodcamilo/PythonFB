class Calculadora:
    def calcular(self, a, b):
        return a + b
class CalculadoraCientifica(Calculadora):
    def calcular(self, a, b, operacao):
        if operacao == "soma":
            return a + b
        elif operacao == "subtracao":
            return a - b
        elif operacao == "multiplicacao":
            return a * b
        elif operacao == "divisao":
            if b != 0:
                return a / b
            else:
                return "Divisão por zero não é permitida."
class Aprendiz:
    def bordao(self):
        pass
class Lcs(Aprendiz):
    def bordao(self):
        return "O meu é rosa!"
class Hnrq(Aprendiz):
        def bordao(self):
            return "Vou fazer uma selfie!"
calc_cientifica = CalculadoraCientifica()
print("Polimorfismo de sobrecarga")
print("Soma:", calc_cientifica.calcular(5, 3, "soma"))
print("Subtração:", calc_cientifica.calcular(10, 4, "subtracao"))
print("Multiplicação:", calc_cientifica.calcular(7, 2, "multiplicacao"))
print("Divisão:", calc_cientifica.calcular(7, 2, "divisao"))
aprendizes = [Lcs(),Hnrq()]
print("\nPolimorfismo de sobreposição:")
for Aprendiz in aprendizes:
    print(Aprendiz.bordao())
