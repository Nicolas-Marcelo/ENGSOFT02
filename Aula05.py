# Pilha
# LIFO

# Primeiro criar uma função

def criar_pilha():
    pilha = []

    return pilha

def verificar_vazio(pilha):
    return len(pilha) == 0

# Empilhar

def push(pilha, item):
    pilha.append(item)

# desempilhar

def pop(pilha):
    if not verificar_vazio(pilha):
        return pilha.pop()

    else:
        return "A pilha está vazia, não é possivel retirar elementos!"

# Topo

def peek(pilha):
    if not verificar_vazio(pilha):
        return pilha[-1]

    else:
        return "A pilha está vazia"

def size(pilha):
    return len(pilha)

pilha = criar_pilha()

push(pilha, 1)
push(pilha, 2)
push(pilha, 3)

print(peek(pilha))

print(pop(pilha))
print(pop(pilha))

push(pilha, 13)

print(pop(pilha))

nomes = criar_pilha()

push(nomes, "Arlindo")
push(nomes, "Renato")
push(nomes, "Enzo")
push(nomes, "Valentina")

print(pop(nomes))
print(pop(nomes))
print(pop(nomes))
print(pop(nomes))

print(verificar_vazio(nomes))
print(pop(nomes))

'''
Implemente yuma função in palindrome 
que recebe uma string como parametro e 
retorna True se a string pe um palindrono^
e False caso ao contrario. um Palindromo é
uma palavra, frase, numero ou qualquer 
outra sequencia de caracteres que é lida 
da mesma forma tanto da esquerda para a
direita como da direita para a esquerda
Exemplos de palindromos
Incluem: arara, radar 12321 e ame o poema
'''

def verefica_palindromo(string):
    # Vai separar a string
    # Primeira coias tirar os espaços e deixar todas as letras maisculas
    string = string.lower().replace(" ", "")
    pilha_pali = criar_pilha()

    # Aqui vai adicionar um valor a pilha_pali
    for i in string:
        push(pilha_pali, i)

    # Criar o reverse, para verificação, mas deixamos ela vazia
    string_reversa = ""

    while not verificar_vazio(pilha_pali):
        # Vai tirando da pilha e jogando na string
        string_reversa += pop(pilha_pali)



    if string_reversa == string :
        print("Certo né")
    else:
        print("Acontece")

    return string_reversa == string

verefica_palindromo()
