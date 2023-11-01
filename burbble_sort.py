# ================================== BURBBLE SORT ==================================
# Lista a ser ordenada
lista = [7, 3, 6, 2, 0]

# Confere o tamanho da lista, para usar como indicador 
tamanho_lista = len(lista)

# Faz o loop 
for i in range(tamanho_lista -1): 
    for j in range (tamanho_lista -1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)
