# ================================================= CLASSE MÂE =================================================
# Vai ser a classe pai, que recebe atributos genericos
class Animal():
    def __init__(self, nome, especie):
        # A diferencia ele associa o nome ao atributo nome
        self.nome = nome
        self.especie = especie

    def emetirSom(self):
        print(f'{self.nome}, faz um som!')

# ============================================== CLASSE CACHORRO ==============================================

from Animal import Animal

# Aqui para importar a classe mãe
class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Sempre usar a função Super()
        super().__init__(nome, especie="Cachorro")
        self.raca = raca

    def emitirSom(self):
        print(f"{self.nome} late. (au au)")

    def buscar(self):
        print(f"{self.nome} busca a bola")

# ============================================== CLASSE GATO ==============================================

from Animal import Animal

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, especie="gato")
        self.cor = cor

    def emitirSom(self):
        print(f"{self.nome} mia. (miauw)")

    def arranhar(self):
        print(f"{self.nome} arranha o sofá")

# ============================================== CODIGO MAIN ==============================================

from Cachorro import Cachorro
from Gato import Gato

# Primeiro cria o nome do objeto
c1 = Cachorro("Byte", "Chihuahua")
g1 = Gato("Get", "Cinza")

c1.emitirSom()
g1.emitirSom()

c1.buscar()
g1.arranhar()
