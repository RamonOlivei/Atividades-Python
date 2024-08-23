class Carro:
    def __init__(self, marca, modelo, cor, cambio, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.cambio = cambio
        self.ano = ano
        self.is_running = False
        self.velocidade = float(0)

    def __str__(self):
        return f"""
        O Carro é:
        marca: {self.marca}
        modelo: {self.modelo}
        cor: {self.cor}
        cambio: {self.cambio}
        ano: {self.ano}

        """
    

    def ligar(self):
        if not self.is_running:
            self.is_running = True
            print(f"Agora o Carro {self.modelo} está ligado!")

    def acelerar(self, velocidade_2):
        if self.is_running:
            self.velocidade =+ velocidade_2
            print(f"E sua Velocidade é {self.velocidade}")

        else:
            print(f"O carro {self.modelo} não está ligado!")


    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"O carro {self.modelo} está parado!")
        else:
            print(f"o carro {self.modelo} está parado! ")


class Moto:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.isrunning = False
        self.velocidade = float(0)


    def __str__(self):
        return f"""
        A moto é:
        marca: {self.marca}
        modelo: {self.modelo}
        cor: {self.cor}
        ano: {self.ano}
        """                




