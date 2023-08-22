'''
Desafio 1
    Crie um conjunto de 1 a 10 e depois imprima o conjunto

Desafio 2
    Crie um dicionario vazio e adicione duas chaves e valores a ele

Desafio 3
    Crie uma tupla com os numero de 1 a 5 e imprima na tela
'''

print("Desafios de conjuntos, dicionarios e tuplas")

def desafio_conjuntos():
    print("Exibição dos conjuntos!")
    conjunto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in conjunto:
        print(i)

def desafio_dicionario():
    print("Exibição dos dicionaios!")
    dicionario = {}
    dicionario['nome'] = 'Nicolas'
    dicionario['idade'] = 19

    for chaves, elementos in dicionario.items():
        print(chaves, " = ", elementos)

def desafio_tuplas():
    print("Exibição das tuplas")
    tuplas = (1, 2, 3, 4, 5)
    for numero in tuplas:
        print(numero)

print(desafio_conjuntos())
print(desafio_dicionario())
print(desafio_tuplas())
