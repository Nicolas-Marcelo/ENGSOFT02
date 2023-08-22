#=================================================== CONJUNTOS =========================================================
import random

def questao1():
    conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    for i in conjunto:
        print(i)

def questao2():
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {3, 4, 5, 6, 7}

    uniao = conjunto1.union(conjunto2)
    interssection = conjunto1.intersection(conjunto2)
    diferenca = conjunto1.difference(conjunto2)

    print(uniao, "\n", interssection, "\n", diferenca)



def questao3():
    digitada = input("Digite uma palavra: ")

    vogais = {'a', 'e', 'i', 'o', 'u'}
    palavra = {digitada}

    for i in digitada:
        if i in vogais:
            print(i)

def questao4():
    lista = {'maça', 'abacaxi', 'pera', 'limao'}
    frutas = {'laranja', 'morango', 'limao'}

    for i in lista:
        if i in frutas:
            print(i)

def questao5():

    numeros = {}
    numeros.add(randrange(0,11))
    print(numeros)



questao5()




