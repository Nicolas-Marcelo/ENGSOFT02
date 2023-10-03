# ATIVIDADE 01
arquivo = open("algo.txt", "a")

i = 1

while i < 20:
    nome = input("DIgite um nome aleatorio: ")
    idade = input("Digite uma idade aleatoria: ")

    arquivo.write(f'A pessoa {nome} tem a idade de {idade} anos\n!')

    arquivo.read()

    i = i + 1

