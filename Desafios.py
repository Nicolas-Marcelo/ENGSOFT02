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

def questao6():

    cores = {"Vermelho", "laranja", "amarelo", "verde", "azul", "Anil", "Violeta"}

    pergunta = input("Digite uma cor e vamos ver se ela faz parte do conjunto do arco-íris: ")
    print(pergunta)

    
    if pergunta in cores:

        print("Está cor está presente no arco-íris! ")

    else:

        print("Está cor não está presente no arco-Iris!")

def questao7():

    print("Este software irá te mostrar os dias dos fins de semana, excluindo dias uteis por baixo dos panos!")

    dias = {"Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"}
    dias.remove("Segunda")
    dias.remove("Terça")
    dias.remove("Quarta")
    dias.remove("Quinta")
    dias.remove("Sexta")

    print(dias)

def questao8():

    conjunto1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    conjunto2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    deferença = conjunto1.difference(conjunto2)

    print(f"Os numeros que tem no conjunto 1 mas não tem no conjunto 2 sãop: ", deferença)

def questao9():

    quantas_notas = int(input("Qual é o numero de notas que você quer registrar: "))
    notas = []

    x = 0
    while(x < quantas_notas):
        notas.append(int(input("Digite suas notas: ")))
        x = x + 1
    
    total = sum(notas)
    media = total / quantas_notas
    
    print("A media total destas notas é: ", media)

def questao10():

    primos = [2, 3, 5, 7, 11, 13, 17]
    numero = int(input("Digite um numero para verificação se ele está presente nos numeros primos de 1 a 20!"))
    
    for i in primos :
        if numero in primos:
            print("Este numero é um numero primo do conjunto de 1 a 20!")
            
        else:
            print("Este numero não é um numero primo do conjunto de 1 a 20!")

#=================================================== DICIONARIOS =========================================================

def question1():
    
    dicionario = {}
    
    dicionario['nome'] = 'Nicolas'
    dicionario['Idade'] = 19
    
    print(dicionario)
    
def question2():
    
    meu_cadastro = {'Nome' : 'Nicolas', 'Idade' : 19 , 'Cidade' : 'Guarapuava'}
    
    print(meu_cadastro)
    
def question3():
    
    produtos = {'Iphone14' : 14.000,
                'Mustang' : 159.000,
                'Casa' : 3500.000}
    
    chaves = produtos.keys()
    valores = produtos.values()
    
    for chaves, valores in produtos.items():
        print(f'produto: {chaves}, seu valor é de {valores}')
        
def question4():
    
    indicador = int(input("Digite um numero 1 a 3 e veja o estado correspondente: "))
    
    estados = {1 : 'Seu estado é o Paraná e sua capital é Curitiba!',
               2 : 'Seu estado é Santa Catarina e sua capital é Blumenau',
               3 : 'Seu estado é Rio Grande do Sul e sua capital é Santa Rosa'}
    
    chaves = estados.keys()
    valores = estados.values()
    
    for indicador in estados:
        if indicador == 1:
            print("deu certo")

    

import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor("black")

t.pensize(2)
t.speed(0)
n = 36
h = 0

for i in range(90):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    
    h+=1/n
    
    t.pencolor(c)
    
    for j in range(5):
        t.forward(i-3)
        t.right(9*5)
        t.left(8)
        
    t.right(115)
turtle.done()



