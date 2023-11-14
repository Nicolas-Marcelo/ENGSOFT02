# ============================================================== CLASSE PRINCIPAL ==============================================================

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


# ============================================================== CLASSE CACHORRO ==============================================================

from Animal import Animal

class Cachorro(Animal):
    def __init__(self, especie, raca, nome, cor, idade, vacinas, pelo):
        super().__init__(especie, raca, nome, cor, idade)
        self.vacinas = vacinas
        self.pelo = pelo

    def emitir_som(self):
        print(f'O seu {self.especie} está latindo')


# ============================================================== CLASSE GATO ==============================================================

from Animal import Animal

class Gato(Animal):
    def __init__(self, especie, raca, nome, cor, idade, pelo, garra):
        super().__init__(especie, raca, nome, cor, idade)
        self.pelo = pelo
        self.garra = garra

    def arranhar(self):
        print(f'O {self.nome} esta arranhando!')

    def emetir_som(self):
        print(f'O {self.nome} esta miando!')

    def cortar_garras(self):
        print("As unhas do seu gato foram cortadas!")


# ============================================================== EXECUÇÃO PRINCIPAL ==============================================================

class Servico:
    def __init__(self, valor=0):
        self.valor = valor

    def serviço(self):
        print("Nossos serviços:\n"
              "Banho:        R$35,00\n"
              "Tosa:         R$30,00\n"
              "Passeio:      R$30,00\n")

    def tosar(self):
        self.valor = self.valor + 30.00

    def banhar(self):
        self.valor = self.valor + 35.00

    def passear(self):
        self.valor = self.valor + 30.00

    def nota(self):
        print("O valor a ser pago é: ", self.valor)

# ============================================================== EXECUÇÃO PRINCIPAL ==============================================================

from Animal import Animal
from Cachorro import Cachorro

def bem_vindo():
    print("Olá sejá bem vindo ao ANR Pet!")
    print("O melhor cuidado para seu Pet!")
    print("Para melhor funcionamento do codigo, escreva tudo em letra Maiuscula\n")




# EXECUÇÃO PRINCIPAL

from Cachorro import Cachorro
from Gato import Gato
from Servico import Servico

def bem_vindo():
    print("Olá sejá bem vindo ao ANR Pet!")
    print("O melhor cuidado para seu Pet!")
    print("Para melhor funcionamento do codigo, escreva tudo em letra Maiuscula\n")

# EXECUÇÃO PRINCIPAL
s1 = Servico(0)

s1.serviço()
bem_vindo()

especie = input("Digite qual é a especie de seu animal: ")
raca = input("Digite a raca de seu animal: ")
nome = input("Digite o nome do seu animal: ")
cor = input("Qual a cor de seu animal: ")
idade = input("Qual a idade de seu animal: ")

especie = especie.upper()
raca = raca.upper()
nome = nome.upper()
cor = cor.upper()



if especie == "CACHORRO":
    vacinas = input("Quantas vacinas seu cachorro ja tomou? ")
    pelo = input("Você deseja tosar seu cachorro? ")
    pelo = pelo.upper()

    especie = especie.lower()
    raca = raca.lower()
    nome = nome.lower()
    cor = cor.lower()

    c1 = Cachorro(especie, raca, nome, cor, idade, vacinas, pelo)

    if pelo == "SIM":
        quanto_cortar = input("Deseja deixar alto, medio ou baixo? ")
        s1.tosar()

    banho = input("Você deseja dar banho em seu cachorro? ")
    banho = pelo.upper()
    if banho == "SIM":
        s1.banhar()

    passear = input("Você deseja passear com seu cachorro! ")
    passear = passear.upper()
    if passear == "SIM":
        s1.passear()

if especie == "GATO":
    garra = input("Deseja cortar as unhas do seu gato? ")
    garra = garra.upper()

    pelo = input("Você deseja tosar seu gato? ")
    pelo = pelo.upper()

    if pelo == "SIM":
        quanto_cortar = input("Deseja deixar alto, medio ou baixo? ")

    especie = especie.lower()
    raca = raca.lower()
    nome = nome.lower()
    cor = cor.lower()

    g1 = Gato(especie, raca, nome, cor, idade, pelo, garra)

    if pelo == "SIM":
        quanto_cortar = input("Deseja deixar alto, medio ou baixo? ")
        s1.tosar()

    banho = input("Você deseja dar banho em seu cachorro? ")
    banho = pelo.upper()
    if banho == "SIM":
        s1.banhar()

    passear = input("Você deseja passear com seu cachorro! ")
    passear = passear.upper()
    if passear == "SIM":
        s1.passear()




