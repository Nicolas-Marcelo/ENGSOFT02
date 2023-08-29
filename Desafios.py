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

    print(estados[indicador])

def question5():

    cidades = {"Guarapuava": 300.000,
               "Ponta Grossa": 200.000,
               "Curitiba": 150.00,
               "Porto Alegre": 300.000,
               "Cidade dos Lagos": 150.000}

    print("Nos temos estas cidades!")
    for i in cidades:
        print(i)

    x = max(cidades, key=cidades.get)

    print(f'Esta é a cidade mais populosa:', x)

def question6():

    calorias = {1 : "Almondega com 120 kcal",
                2 : "Bife de alcategra com 268 kcal",
                3 : "Carne bovina com 250 kcal"}

    indicador = int(input("Digite um numero: "))

    print(calorias[indicador], " Este é o alimento correspondete ao seu numero!")

def question7():

    animais = {"Cachorro" : "Mamifero",
               "Passaro" : "Ave",
               "Dinossauro" : "Reptil",
               "Andorinha" : "Ave",
               "Lagarto" : "Reptil"}

    chaves = animais.keys()

    for chaves in animais:
        print(chaves)

def question8():

    paises = {"Brasil" : "Bandeira?",
              "Colombia" : "Bandeira?",
              "Paris" : "Bandeira?",
              "Portugal" : "Bandeira?",
              "Canadá" : "Bandeira?"}

    chaves = paises.keys()

    for chaves in paises:
        print(chaves)

def question9():

    frutas = {"Morango" : "Vermelho",
              "Laranja" : "Laranja",
              "Limão" : "Verde",
              "Pera" : "Amarelo",
              "Jambo" : "Rosa",}

    chaves = frutas.keys()
    valores = frutas.values()

    for chaves, valores in frutas.items():

        print(f'A fruta é {chaves} e a cor é {valores}!')

def question10():

    jogos = {1 : "Truco com 4 pessoas necessarias para jogar",
             2 : "Xadrez com 2 pessaos necessarias para jogar",
             3 : "Volêi com 12 pessoas necessarias para jogar"}

    indicador = int(input("Digite o numero que vamos lhe mostrar o jogo correspondete: "))

    print(jogos[indicador])

#=================================================== TUPLAS =========================================================

def question01():

    tupla = (1, 2, 3, 4, 5)
    print(tupla)

def question02():

    paises = ("Brasil", "Russia", "India")

    print(paises[2])

def question03():

    conta = (1500.00, 100.00, 1600.00)

    print(f'O valor total da conta é: {conta[1]}'
          f'O valor da taxa de serviço é: {conta[2]}'
          f'O valor total da compra é: {conta[3]}')

def question04():

    nomes = ("Nicolas", "Isabelly", "Ana", "Marcelo", "Flavia")
    indicador = int(input("Digite um numero: "))

    print(nomes[indicador])

def question05():

    notas = (10, 9, 6, 10)

    media = sum(notas) / len(notas)

    print("A media das notas é: ", media)

def question06():

    cores = ("Vermelho", "laranja", "amarelo", "verde", "azul", "Anil", "Violeta")

    pergunta = input("Digite uma cor e vamos ver se ela faz parte do conjunto do arco-íris: ")
    print(pergunta)

    if pergunta in cores:

        print("Está cor está presente no arco-íris! ")

    else:

        print("Está cor não está presente no arco-Iris!")

def question07():

    temperaturas = (30.3, 36.9, 12.3, 05.3, 15.9, 97.0)

    maior = max(temperaturas)
    minima = min(temperaturas)

    print(f'A maxima dos dias da semana é: {maior}'
          f'A minima dos dias da semana é: {minima}')

def question08():

    frutas = ("Morango e sua cor é Vermelho\n", "Laranja e sua cor é Laranjan\n", "Limão e sua cor é Verde\n", "Pera e sua cor é Amarelo\n", "Jambo e sua cor é Rosa\n",)

    print(frutas)
    
def question09():
    
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tupla2 = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    
    intercessao = tupla1.intercession(tupla2)
    print(intercessao)
    
def question10():
    
    letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u")
    vogais = ("a", "e", "i", "o", "u")
    
    diferenca = letras.diference(vogais)
    
    print(diferenca)
