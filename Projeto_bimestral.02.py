# =================================================== CLASSE MÃE ===================================================

class Animal:
    def __init__(self, especie, raca, nome, cor, idade):
        self.especie = especie
        self.raca = raca
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def passer(self):
        print(f'O seu {self.especie}, {self.nome} está indo passear!')

    def tosar(self):
        print(f'O seu {self.especie}, {self.nome} está indo para a tosa!')

    def banhar(self):
        print(f'O seu {self.especie}, {self.nome} está indo para o baanho')

    def imitir_som(self):
        print(f'O seu {self.especie}, {self.nome} está emitindo som!')

# =================================================== CLASSE CACHORRO ===================================================

from Animal import Animal

class Cachorro(Animal):
    def __init__(self, especie, raca , nome, cor, idade, vacinas, pelo):
        super().__init__(especie, raca, nome, cor, idade)
        self.vacinas = vacinas
        self.pelo = pelo

    def latir(self):
        print(f'O seu {self.especie} está latindo')

# =================================================== CLASSE GATO ===================================================

from Animal import Animal

class Gato(Animal):
    def __init__(self, especie, raca, nome, cor, idade, pelo, garra):
        super().__init__(especie, raca, nome, cor, idade)
        self.pelo = pelo
        self.garra = garra

    def arranhar(self):
        print(f'O {self.nome} esta arranhando!')

    def miar(self):
        print(f'O {self.nome} esta miando!')

    def cortar_garras(self):
        print("As unhas do seu gato foram cortadas!")

# =================================================== EXECUÇÃO PRINCIPAL ===================================================

from Animal import Animal
from Cachorro import Cachorro

def bem_vindo():
    print("Olá sejá bem vindo ao ANR Pet!")
    print("O melhor cuidado para seu Pet!")
    print("Para melhor funcionamento do codigo, escreva tudo em letra Maiuscula\n")




# EXECUÇÃO PRINCIPAL

bem_vindo()

especie = input("Digite qual é a especie de seu animal: ")
especie = especie.upper()

raca = input("Digite a raca de seu animal: ")
raca = raca.upper()

nome = input("Digite o nome do seu animal: ")
nome = nome.upper()

cor = input("Qual a cor de seu animal: ")
cor = cor.upper()

idade = input("Qual a idade de seu animal: ")
cor = cor.upper()

if especie == "CACHORRO":
    vacinas = input("Quantas vacinas seu cachorro ja tomou? ")
    pelo = input("Você deseja tosar seu cachorro? ")
    pelo = pelo.upper()

    if pelo == "SIM":
        quanto_cortar = input("Deseja deixar alto, medio ou baixo? ")
    else:
        pass

if especie == "GATO":
    garra = input("Deseja cortar as unhas do seu gato? ")
    garra = garra.upper()

    pelo = input("Você deseja tosar seu gato? ")
    pelo = pelo.upper()

    if pelo == "SIM":
        quanto_cortar = input("Deseja deixar alto, medio ou baixo? ")
    else:
        pass



else:
    pass











a1 = Animal(especie, raca, nome, cor, idade)
