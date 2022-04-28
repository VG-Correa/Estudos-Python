class Carro:
    def __init__(self,marca,modelo,cor,combustível,ligado,velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustível = combustível
        self.ligado = False
        self.velocidade = 0

    def Ligar(self):
        if self.ligado:
            print(f"O {self.modelo} já está ligado!! nada acontece.")
        else:
            print(f"O {self.modelo} foi ligado!!")
            self.ligado = True
        
    
    def Desligar(self):
        if not(self.ligado):
            print(f"O {self.modelo} já está desligado!! nada acontece.")
        else:
            self.ligado = False
            print(f"O {self.modelo} foi desligado!")

    def Acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"O {self.modelo} está a {self.velocidade}km/h")
        else:
            print(f"Não é possível acelerar o {self.modelo} com ele desligado!! Ligue-o primeiro!")
    
    def Frear(self):
        if self.velocidade > 0:
            self.velocidade -= 1
            print(f"O {self.modelo} está a {self.velocidade}km/h")
        else:
            print(f"O {self.modelo} não está em movimento! impossível frear")