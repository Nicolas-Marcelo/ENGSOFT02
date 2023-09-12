uma_lista = ["UM", "DOIS", "TRES", "QUATRO", "CINCO", "SEIS"]

print("Começando contagem regressiva")

# for i in uma_lista:

# função verifica tem elementos, condição
def is_empty(uma_lista):
    return len(uma_lista) == 0

# Enquanto a lista não estiver vazia, ele desinfilerando
while not is_empty(uma_lista):
    print("Contegem em ",uma_lista.pop(0))

print(len(uma_lista))

