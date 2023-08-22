def aula_02_conjunto():

# Conjuntos

# Crinado um conjunto vazio
    meu_conjunto = set()                         # Set deixa o conjunto com vazio

    meu_conjunto_dois = {1,2,3,4}

    meu_conjunto_dois.add(8)                     # lista.add() é para adicionar um elemento

    meu_conjunto_dois.remove(2)                  # Lista.remove() è para tirar um elemento pelo seu valor

# Verificando se há um elemento na lista

    if 3 in meu_conjunto_dois:
        print("O conjunto contém o elemento 3!")

# Operaçôes da Loli

# Famosa UNIÂO
    conjunto1 = {1, 2, 3}

    conjunto2 = {9, 10, 11}

    conjunto1.union(conjunto2)                     # Conjunto1.unnion(conjunto2) para fazer a união de conjuntos

# Intersecção

    intersecao = conjunto1.intersection(conjunto2) # Conjunto1.intersection(conjunto2) retorna oque há de comum entre 1 e outro
    print(intersecao)

# DIferencia

    diferenca = conjunto1.difference(conjunto2)    # Conjunto1.diference(conjunto2) para ver a diferença entre 1 conjunto e outro
    print(diferenca)                               # Bastante importante para não deixar valores repetidos

aula_02_conjunto()

def aula_03_dicioarios():

# DIcionarios

    meu_dicionario = {}
    meu_dicionario2 = {'nome': 'João', 'idade': 30, 'cidade': 'guarapuava',}

# Adicionando elementos

    meu_dicionario2['profissao'] = 'programador'

# Removendo elementos

    del meu_dicionario2['cidade']

# Verificando se uma chave existe

    if 'idade' in meu_dicionario2:
        print("A chave 'idade' existe no dicionario!")

# Como obter apenas as chaves ou valores de um dicionario

    chaves = meu_dicionario2.keys()

    valores = meu_dicionario2.values()

    for chaves,valores in meu_dicionario2.items():
        print(chaves, " = ",valores)

# Mesclar dicionarios

    meu_dicionario3 = {'sobrenome': 'Silva', 'telefore': 123456789}
    meu_dicionario2.update(meu_dicionario3)

    print(meu_dicionario2)

aula_03_dicioarios()

def aula_04_tuplas():

# Tuplas

    minha_tupla = ()
    minha_tupla2 = (1, 2, 3, 'quatro', 'cinco', 6.0)

# Concatevar tuplas

    minha_tupla3 = ('a', 'b', 'c')
    nova_tupla = minha_tupla2 + minha_tupla3

# Verificar a existencia de um valor na tupla

    if 'quatro' in minha_tupla2:
        print("O elemento 'quatro' está existente na minha_tupla_dois!")

# Percorrer a tupla

    for elemento in minha_tupla2:
        print(elemento)

print(aula_04_tuplas())
