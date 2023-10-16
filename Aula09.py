# ======================================================== CLASSE MÃE ========================================================
from abc import ABC, abstractmethod

class Pessoa (ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def saudar (self):
        pass

    # Está classe é abstrata então não pode ter objetos
# ======================================================== CLASSE ALUNO ========================================================
from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def saudar(self):
        return f'Olá, bom dia!! Turu bom?? Eu sou um aluno {self.nome}'
# ======================================================== CLASSE PROFESSOR ========================================================
from Pessoa import Pessoa

class Professor (Pessoa):
    def __init__(self, nome):
        # Assim eu atribuo o nome daqui para a classe mãe
        super().__init__(nome)

    # Se torna obrigatorio o saudar por estar na classemãe
    def saudar(self):
        return f'Olá, bom dia!! Turu bom?? Eu sou o professor {self.nome}'
# # ======================================================== MAIN ========================================================
from Professor import Professor
from Aluno import Aluno

p1 = Professor("Alan Turing")
a1 = Aluno("Bill")

print(p1.saudar())
print(a1.saudar())
