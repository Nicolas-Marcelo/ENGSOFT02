# ============================================== ATVIDADE 1 ============================================== 

class Carro():
    def __init__(self, modelo, ano):
        self._modelo = modelo
        self._ano = ano

    def andar (self):
        print(f'Eu tenh um carro {self._modelo} ano {self._ano}')

# ============================================== ATVIDADE 2 ============================================== 

class Carro():
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano

    def andar (self):
        print(f'Eu tenh um carro {self._modelo} ano {self._ano}')
      
# ============================================== ATVIDADE 3 ============================================== 

class Veiculo():
    def __init__(self, tipo, velocidade):
        self.velocidade = velocidade
        self.tipo = tipo

    def especificar(self):
        if self.tipo == "Fusca":
            print(f'Seu veiculo que é um/a {self.tipo} está andando a velocidade {self.velocidade} cavalos')

        if self.tipo == "Motoqueiro fantasma":
            print(f'Seu veiculo que é um/a {self.tipo} está andando a velocidade {self.velocidade} cilindradas')

from Veiculo import Veiculo

class Carro (Veiculo):
    def __init__(self, tipo, cavalos):
        super().__init__(tipo, cavalos)

from Veiculo import Veiculo

class Moto (Veiculo):
    def __init__(self, tipo, cilindradas):
        super().__init__(tipo, cilindradas)

from Carro import Carro
from Moto import Moto

c1 = Carro("Fusca", 1000)
m1 = Moto("Motoqueiro fantasma", 2000)

c1.especificar()
m1.especificar()

# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
