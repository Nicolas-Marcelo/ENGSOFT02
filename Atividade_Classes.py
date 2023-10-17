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

# ============================================== ATVIDADE 4 ============================================== 
class Veiculo():
    def __init__(self, tipo, velocidade, ano, cor, km_rodado):
        self.velocidade = velocidade
        self.tipo = tipo
        self.ano = ano
        self.cor = cor
        self.km_rodado = km_rodado

    def especificar(self):
        if self.tipo == "Fusca":
            print(f'Seu veiculo que é um/a {self.tipo} está andando a velocidade {self.velocidade} cavalos')

        if self.tipo == "Motoqueiro fantasma":
            print(f'Seu veiculo que é um/a {self.tipo} está andando a velocidade {self.velocidade} cilindradas')

    def descricao(self):
        print(f'Seu veiculo modelo {self.tipo} do ano {self.ano} de cor {self.cor}, está andando a velocidade de {self.velocidade} '
              f'e está com contador em {self.km_rodado} KMs rodados!')

from Veiculo import Veiculo

class Carro (Veiculo):
    def __init__(self, tipo, cavalos, ano, cor, km_rodado):
        super().__init__(tipo, cavalos, ano, cor, km_rodado)

    def descricao(self):
        print(f'Sua {self.tipo} fabricada no ano {self.ano} tem a cor {self.cor}, a moto tem sua velocidade maxima de {self.velocidade}'
              f'e hoje atinge o feito de {self.km_rodado}')

from Veiculo import Veiculo

class Moto (Veiculo):
    def __init__(self, tipo, cilindradas, ano, cor, km_rodado):
        super().__init__(tipo, cilindradas, ano, cor, km_rodado)

    def descricao(self):
        print(f'Seu veiculo modelo {self.tipo} fabricada no ano de {self.ano} tem a cor de {self.cor}'
              f'e já atingiu a velocidade de {self.velocidade} e agora está com {self.km_rodado} KMs rodados')
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
# ============================================== ATVIDADE 1 ============================================== 
