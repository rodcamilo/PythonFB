class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} está Ligado!")
        else:
            print(f"O {self.modelo} já estava Ligado!")
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O {self.modelo} está Desligado!")
        else:
            print(f"O {self.modelo} já estava Desligado!")
    def exibir_infos(self):
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        estado = "Ligado" if self.ligado else "Desligado"
        print(f"Estado: {estado}")
#criar objeto
meu_carro = Carro("Toyota Corolla", 2023, "Prata")
#exibir objeto
meu_carro.exibir_infos()
#ligando carro
meu_carro.ligar()
#desligar carro
meu_carro.desligar()
