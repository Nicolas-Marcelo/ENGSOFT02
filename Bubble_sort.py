def bem_vindo():
    print("Seja bem vindo ao software ...............")

def bubble_sort():
    tamanho_lista = len(lista_datas)

    for i in range(tamanho_lista -1): 
        for j in range (tamanho_lista -1):
            if lista_datas[j] > lista_datas[j + 1]:
                lista_datas[j], lista_datas[j + 1] = lista_datas[j + 1], lista_datas[j]

def lista_organizada():
    print("Nosso sistema informa que essa é a lista de funcionarios e suas datas de admissões por data!")

    for i in lista_datas:
        print(f'No formato DD/MM/AAAA {i}!')
        

rodadas = 0
lista_datas = []

while rodadas < 3:

    idade = int(input("No formato DD/MM/AAAA.\nColoque sua data de admissão: "))    
    lista_datas.append(idade)
    rodadas = rodadas + 1

bem_vindo()
bubble_sort()
lista_organizada()

