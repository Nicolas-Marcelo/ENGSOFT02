import os

# No plano inicial o software vai ser algo para me ajudar no serviço
# Com cadastramento de fotos por um sistema classificando direto a hora que foi tirada a foto
# De que obra ela pertence e demais coisas das fotos
# E outra função é conferir equipamentos e funcionarios 

def boas_vinda() :
    print("Seja bem vindo ao software de auxilio ao auxiliar administrativo da Dalba!")
    print("Dentro do software temos varias funçoes, digite o numero correspondente da função desejada!\n"
          "( 1 ) Para anexar as fotos!\n"
          "( 2 ) Para conferição de funcionarios!\n"
          "( 3 ) Para conferição de equipamentos!\n")
    
def pausa():
    os.system("cls")

# Esta variavel armazena o numero da função desejada
função_desejada = int(input("Digite o numero da função desejada: "))



'''
========================================= OUTPUT ============================================
'''
while True:
    # Da as primeira informações do software
    boas_vinda()
    
    # Classifica a função que vai ser vista
    função_desejada
    
    pausa()

    # Primeiro IF para cadastramento de fotos 
    if função_desejada == 1:
        print("Você escolheu o cadastramento de fotos!")
        

        # LIstando todas aso obras
        lista_de_obras = {"( 1 )" : "OB0820", 
                          "( 2 )" : "OB0821",
                          "( 3 )" : "OB0825",
                          "( 4 )" : "OB0826",
                          "( 5 )" : "OB0794"}
        
        chaves = lista_de_obras.keys()
        valores = lista_de_obras.values()
        
        for chaves, valores in lista_de_obras.items():
            print(f'Digite {chaves} para selecionar a obra {valores}')
            
        # Qual obra ??
        obra = int(input("De qual obra são as fotos? "))
        print(obra)
        
        # Salvando as fotos 
        if obra == 1:
            print("Digite o nome das fotos desejadas para anexar!")
            
            # Lista com as fotos
            fotos_OB0820 = []
            
            # Contagem do While
            contagem = int(input("Digite quantas fotos você quer anexar: "))
            print(f'Você salvara {contagem} fotos!')
            
            i = 1
            
            while i <= contagem:
                nome_foto = input("Digite o nome da foto")
                print(f'Este é o nome da foto {nome_foto}!')
                
                # Adicionando foto
                fotos_OB0820.append(nome_foto)
            
            # Mostrando fotos salvas
            print("Essas foram as fotos salvas!")
            
            for i in fotos_OB0820:
                print(f'Estas são as fotos: {i}')
                
            break
            
        elif obra == 2:
            print("Digite o nome das fotos desejadas para anexar!")
            
            # Lista com as fotos
            fotos_OB0821 = []
            
            # Contagem do While
            contagem = int(input("Digite quantas fotos você quer anexar: "))
            print(f'Você salvara {contagem} fotos!')
            
            i = 1
            
            while i <= contagem:
                nome_foto = input("Digite o nome da foto: ")
                print(f'Este é o nome da foto {nome_foto}!')
                
                # Adicionando foto
                fotos_OB0821.append(nome_foto)
                i = i + 1
            
            # Mostrando fotos salvas
            print("Essas foram as fotos salvas!")
            
            for i in fotos_OB0821:
                print(f'Estas são as fotos: {fotos_OB0821}')
            
            break
        
        elif obra == 3:
            print("[]")
            
            # Lista com as fotos
            fotos_OB0825 = []
            
            # Contagem do While
            contagem = int(input("Digite quantas fotos você quer anexar: "))
            print(f'Você salvara {contagem} fotos!')
            
            i = 1
            
            while i <= contagem:
                nome_foto = input("Digite o nome da foto")
                print(f'Este é o nome da foto {nome_foto}!')
                
                # Adicionando foto
                fotos_OB0825.append(nome_foto)
                i = i + 1
            
            # Mostrando fotos salvas
            print("Essas foram as fotos salvas!")
            
            for i in fotos_OB0825:
                print(f'Estas são as fotos: {i}')
            
            break
        
        elif obra == 4:
            print("Digite o nome das fotos desejadas para anexar!")
            
            # Lista com as fotos
            fotos_OB0826 = []
            
            # Contagem do While
            contagem = int(input("Digite quantas fotos você quer anexar: "))
            print(f'Você salvara {contagem} fotos!')
            
            i = 1
            
            while i <= contagem:
                nome_foto = input("Digite o nome da foto")
                print(f'Este é o nome da foto {nome_foto}!')
                
                # Adicionando foto
                fotos_OB0826.append(nome_foto)
                i = i + 1
            
            # Mostrando fotos salvas
            print("Essas foram as fotos salvas!")
            
            for i in fotos_OB0826:
                print(f'Estas são as fotos: {i}')
                
            break
            
        elif obra == 5:
            print("Digite o nome das fotos desejadas para anexar!")
        
            # Lista com as fotos
            fotos_OB0794 = []
            
            # Contagem do While
            contagem = int(input("Digite quantas fotos você quer anexar: "))
            print(f'Você salvara {contagem} fotos!')
            
            i = 1
            
            while i <= contagem:
                nome_foto = input("Digite o nome da foto: ")
                print(f'Este é o nome da foto {nome_foto}!')
                
                # Adicionando foto
                fotos_OB0794.append(nome_foto)
                i = i + 1
            
            # Mostrando fotos salvas
            print("Essas foram as fotos salvas!")
            
            for i in fotos_OB0794:
                print(f'Estas são as fotos: {i}')
                
            break
                
        else : 
            print("Digite um numero que pertence a lista!")   
    
    elif função_desejada == 2:
        print("Você selecionou a opção de verificação de funcionarios!")
        
        # Seleção de qual lista quer ver
        lista = int(input("Digite a OB desejada: "))
        print("Selecionada a OB", lista)
        
        pausa()
        
        if lista == 820:
            print("Funiconarios da OB0820:")
            
            funcionarios_OB0820 = { "Antonio" : "Rasteleiro",
                                    "Adriano" : "Rasteleiro",
                                    "Josue" : "Meseiro",
                                    "Jair" : "Servente",
                                    "João Paulo" : "Rasteleiro",
                                    "Pedro" : "Encarregado de obras",
                                    "Dirceu" : "Motorista",
                                    "Tiago" : "Apontador",
                                    "Irineu" : "Topografico"}
            
            chaves = funcionarios_OB0820.keys()
            valores = funcionarios_OB0820.values()
            
            # Apresentando os funcionarios 
            
            i = 1
            
            for chaves, valores in funcionarios_OB0820.items():
                
                print(f'({i}) Funionario {chaves} com a função de {valores}')
                i = i + 1
                
            break
                
        elif lista == 821:
            print("Funionarios da OB0821: ")
            
            funcionarios_OB0821 = { "Antonio" : "Rasteleiro",
                                    "Adriano" : "Rasteleiro",
                                    "Josue" : "Meseiro",
                                    "Jair" : "Servente",
                                    "João Paulo" : "Rasteleiro",
                                    "Pedro" : "Encarregado de obras",
                                    "Dirceu" : "Mororista",
                                    "Tiago" : "Apontador",
                                    "Irineu" : "Topografico"}
            
            chaves = funcionarios_OB0821.keys()
            valores = funcionarios_OB0821.values()
            
            i = 1
            
            # Apresentando os funcionarios 
            for chaves, valores in funcionarios_OB0821.items():
                
                print(f'({i}) Funionario {chaves} com a função de {valores}')
                i = i + 1
                
        elif lista == 825:
            print("Funionarios da OB0825: ")
            
            funcionarios_OB0825 = { "Antonio" : "Rasteleiro",
                                    "Adriano" : "Rasteleiro",
                                    "Josue" : "Meseiro",
                                    "Jair" : "Servente",
                                    "João Paulo" : "Rasteleiro",
                                    "Pedro" : "Encarregado de obras",
                                    "Dirceu" : "Mororista",
                                    "Tiago" : "Apontador",
                                    "Irineu" : "Topografico"}
            
            chaves = funcionarios_OB0825.keys()
            valores = funcionarios_OB0825.values()
            
            i = 1
            
            # Apresentando os funcionarios 
            for chaves, valores in funcionarios_OB0825.items():
                
                print(f'({i}) Funionario {chaves} com a função de {valores}')
                i = i + 1
                
        elif lista == 826:
            print("Funionarios da OB0826: ")
            
            funcionarios_OB0826 = { "Antonio" : "Rasteleiro",
                                    "Adriano" : "Rasteleiro",
                                    "Josue" : "Meseiro",
                                    "Jair" : "Servente",
                                    "João Paulo" : "Rasteleiro",
                                    "Pedro" : "Encarregado de obras",
                                    "Dirceu" : "Mororista",
                                    "Tiago" : "Apontador",
                                    "Irineu" : "Topografico"}
            
            chaves = funcionarios_OB0826.keys()
            valores = funcionarios_OB0826.values()
            
            i = 1
            
            # Apresentando os funcionarios 
            for chaves, valores in funcionarios_OB0826.items():
                
                print(f'({i}) Funionario {chaves} com a função de {valores}')
                i = i + 1
                
            funcionario_procurado = input("Digite qual funcionario você está procurando: ")
            print(f'o funcionario {funcionario_procurado} está na obra e com a função de {funcionarios_OB0826[funcionario_procurado]}!')
            
            break
                
        elif lista == 794:
            print("Funionarios da OB0794: ")
            
            funcionarios_OB0794 = { "Antonio" : "Rasteleiro",
                                    "Adriano" : "Rasteleiro",
                                    "Josue" : "Meseiro",
                                    "Jair" : "Servente",
                                    "João Paulo" : "Rasteleiro",
                                    "Pedro" : "Encarregado de obras",
                                    "Dirceu" : "Mororista",
                                    "Tiago" : "Apontador",
                                    "Irineu" : "Topografico"}
            
            chaves = funcionarios_OB0794.keys()
            valores = funcionarios_OB0794.values()
            
            i = 1
            
            # Apresentando os funcionarios 
            for chaves, valores in funcionarios_OB0794.items():
            
                print(f'({i}) Funionario {chaves} com a função de {valores}')
                i = i + 1
                
            funcionario_procurado = input("Digite qual funcionario você está procurando: ")
            print(f'o funcionario {funcionario_procurado} está na obra e com a função de {funcionarios_OB0794[funcionario_procurado]}!')
            
            # Preciso conferir se um item está a lista

        else :
            print("Digite o indice da OB correto!")
        
        
    elif função_desejada == 3:
        pass

    else:
        pass
    


    
    
    
    
