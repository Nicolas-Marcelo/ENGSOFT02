"""
ALUNOS: NICOLAS MARCELO E ANA PONTAROLO
"""

import os

# No plano inicial o software vai ser algo para me ajudar no serviço
# Com cadastramento de fotos por um sistema classificando direto a hora que foi tirada a foto
# De que obra ela pertence e demais coisas das fotos
# E outra função é conferir equipamentos e funcionarios 

print("Digite seu nome e sua senha!")
nome = input("Nome: ")
senha = int(input("senha: "))

def boas_vinda() :
    print(f'Seja bem vindo, este é o software de auxilio ao auxiliar administrativo da Dalba!')
    print("Dentro do software temos varias funçoes, digite o numero correspondente da função desejada!\n"
          "( 1 ) Para anexar as fotos!\n"
          "( 2 ) Para conferição de funcionarios!\n"
          "( 3 ) Para conferição de equipamentos!\n")
    
def pausa():
    os.system("cls")
    
def puxa_pausa():
    input("\n========================== Digite ENTER para continuar! ==============================\n")
    
def fatorial (n):
    total, k = 1, 1
    
    while k <= n:
        total, k = total * k, k + 1
        
    return total

puxa_pausa()

senha_certa = 123456789

'''
========================================= OUTPUT ============================================
'''
def tudo():
    while True:
        # Da as primeira informações do software
        boas_vinda()
        
        # Classifica a função que vai ser vista
        função_desejada = int(input("Digite o numero da função desejada: "))
        
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
                # Lista com as fotos
                fotos_OB0820 = []
                
                # Contagem do While
                contagem = int(input("Digite quantas fotos você quer anexar: "))
                print(f'Você salvara {contagem} fotos!')
                
                puxa_pausa()
                
                print("Digite o nome das fotos desejadas para anexar!")
                
                i = 1
                
                while contagem >= i:
                    nome_foto = input("Digite o nome da foto: ")
                    
                    # Adicionando foto
                    fotos_OB0820.append(nome_foto)
                    i = i + 1
                    
                puxa_pausa()
                
                # Mostrando fotos salvas
                print("Essas foram as fotos salvas!")
                
                for i in fotos_OB0820:
                    print(f'Estas são as fotos: {i}')
                
                puxa_pausa()
                
                operador = int(input(("Digite qualquer tecla numerica para voltar a pagina de inicio! ")))
                
                if operador == 1:
                    break
                
                else:    
                    return tudo()
                    puxa_pausa()
                
            elif obra == 2:
                # Lista com as fotos
                fotos_OB0821 = []
                
                # Contagem do While
                contagem = int(input("Digite quantas fotos você quer anexar: "))
                print(f'Você salvara {contagem} fotos!')
                
                puxa_pausa()
                
                print("Digite o nome das fotos desejadas para anexar!")
                
                i = 1
                
                while contagem >= i:
                    nome_foto = input("Digite o nome da foto: ")
                    
                    # Adicionando foto
                    fotos_OB0821.append(nome_foto)
                    i = i + 1
                    
                puxa_pausa()
                
                # Mostrando fotos salvas
                print("Essas foram as fotos salvas!")
                
                for i in fotos_OB0821:
                    print(f'Estas são as fotos: {i}')
                    
                puxa_pausa()
                
                operador = int(input(("Digite qualquer tecla numerica para voltar a pagina de inicio! ")))
                
                if operador == 1:
                    break
                
                else:    
                    return tudo()
                    puxa_pausa()
                
            
            elif obra == 3:
                # Lista com as fotos
                fotos_OB0825 = []
                
                # Contagem do While
                contagem = int(input("Digite quantas fotos você quer anexar: "))
                print(f'Você salvara {contagem} fotos!')
                
                puxa_pausa()
                
                print("Digite o nome das fotos desejadas para anexar!")
                
                i = 1
                
                while contagem >= i:
                    nome_foto = input("Digite o nome da foto: ")
                    
                    # Adicionando foto
                    fotos_OB0825.append(nome_foto)
                    i = i + 1
                    
                puxa_pausa()
                
                # Mostrando fotos salvas
                print("Essas foram as fotos salvas!")
                
                for i in fotos_OB0825:
                    print(f'Estas são as fotos: {i}')
                    
                puxa_pausa()
                
                operador = int(input(("Digite qualquer tecla numerica para voltar a pagina de inicio! ")))
                
                if operador == 1:
                    break
                
                else:    
                    return tudo()
                    
                    puxa_pausa()
                
            
            elif obra == 4:
                # Lista com as fotos
                fotos_OB0826 = []
                
                # Contagem do While
                contagem = int(input("Digite quantas fotos você quer anexar: "))
                print(f'Você salvara {contagem} fotos!')
                
                puxa_pausa()
                
                print("Digite o nome das fotos desejadas para anexar!")
                
                i = 1
                
                while contagem >= i:
                    nome_foto = input("Digite o nome da foto: ")
                    
                    # Adicionando foto
                    fotos_OB0826.append(nome_foto)
                    i = i + 1
                    
                puxa_pausa()
                
                # Mostrando fotos salvas
                print("Essas foram as fotos salvas!")
                
                for i in fotos_OB0826:
                    print(f'Estas são as fotos: {i}')
                    
                puxa_pausa()
                
                operador = int(input(("Digite qualquer tecla numerica para voltar a pagina de inicio! ")))
                
                if operador == 1:
                    break
                
                else:    
                    return tudo()
                    
                    puxa_pausa()
                
                
            elif obra == 5:
                # Lista com as fotos
                fotos_OB0794 = []
                
                # Contagem do While
                contagem = int(input("Digite quantas fotos você quer anexar: "))
                print(f'Você salvara {contagem} fotos!')
                
                puxa_pausa()
                
                print("Digite o nome das fotos desejadas para anexar!")
                
                i = 1
                
                while contagem >= i:
                    nome_foto = input("Digite o nome da foto: ")
                    
                    # Adicionando foto
                    fotos_OB0794.append(nome_foto)
                    i = i + 1
                    
                puxa_pausa()
                
                # Mostrando fotos salvas
                print("Essas foram as fotos salvas!")
                
                for i in fotos_OB0794:
                    print(f'Estas são as fotos: {i}')
                    
                puxa_pausa()
                
                operador = int(input(("Digite qualquer tecla numerica para voltar a pagina de inicio! ")))
                
                if operador == 1:
                    break
                
                else:    
                    return tudo()
                    puxa_pausa()
                
                    
            else : 
                print("Digite um numero que pertence a lista!")   
        
        elif função_desejada == 2:
            print("Você selecionou a opção de verificação de funcionarios!")
            
            # Seleção de qual lista quer ver
            lista = int(input("Digite a OB desejada: "))
            
            puxa_pausa()
            
            if lista == 820:
                print("Funionarios da OB0820: ")
                
                funcionarios_OB0820 = { "Antonio" : "Rasteleiro",
                                        "Adriano" : "Rasteleiro",
                                        "Josue" : "Meseiro",
                                        "Jair" : "Servente",
                                        "João Paulo" : "Rasteleiro",
                                        "Pedro" : "Encarregado de obras",
                                        "Dirceu" : "Mororista",
                                        "Tiago" : "Apontador",
                                        "Irineu" : "Topografico"}
                
                lista_funcionarios_OB0820 = {"Antonio", "Adriano", "Josue", "Jair", "João Paulo", "Pedro", "Dirceu", "Taigo", "Irineu"}
                
                chaves = funcionarios_OB0820.keys()
                valores = funcionarios_OB0820.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in funcionarios_OB0820.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    funcionario_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {funcionario_procurado} está na obra e com a função de {funcionarios_OB0820[funcionario_procurado]}!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(funcionario_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_funcionarios_OB0820.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()
                    
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
                
                lista_funcionarios_OB0821 = {"Antonio", "Adriano", "Josue", "Jair", "João Paulo", "Pedro", "Dirceu", "Taigo", "Irineu"}
                
                chaves = funcionarios_OB0821.keys()
                valores = funcionarios_OB0821.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in funcionarios_OB0821.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    funcionario_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {funcionario_procurado} está na obra e com a função de {funcionarios_OB0821[funcionario_procurado]}!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(funcionario_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_funcionarios_OB0821.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()

                    
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
                
                lista_funcionarios_OB0825 = {"Antonio", "Adriano", "Josue", "Jair", "João Paulo", "Pedro", "Dirceu", "Taigo", "Irineu"}
                
                chaves = funcionarios_OB0825.keys()
                valores = funcionarios_OB0825.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in funcionarios_OB0825.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    funcionario_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {funcionario_procurado} está na obra e com a função de {funcionarios_OB0825[funcionario_procurado]}!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(funcionario_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_funcionarios_OB0825.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()

                    
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
                
                lista_funcionarios_OB0826 = {"Antonio", "Adriano", "Josue", "Jair", "João Paulo", "Pedro", "Dirceu", "Taigo", "Irineu"}
                
                chaves = funcionarios_OB0826.keys()
                valores = funcionarios_OB0826.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in funcionarios_OB0826.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    funcionario_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {funcionario_procurado} está na obra e com a função de {funcionarios_OB0826[funcionario_procurado]}!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(funcionario_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_funcionarios_OB0826.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()

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
                
                lista_funcionarios_OB0794 = {"Antonio", "Adriano", "Josue", "Jair", "João Paulo", "Pedro", "Dirceu", "Taigo", "Irineu"}
                
                chaves = funcionarios_OB0794.keys()
                valores = funcionarios_OB0794.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in funcionarios_OB0794.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    funcionario_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {funcionario_procurado} está na obra e com a função de {funcionarios_OB0794[funcionario_procurado]}!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(funcionario_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_funcionarios_OB0794.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()

            else :

                print("Digite o indice da OB correto!")
            
        elif função_desejada == 3:
            
            print("Você selecionou a opção de verificação de funcionarios!")

            # Seleção de qual lista quer ver
            lista = int(input("Digite a OB desejada: "))
            print("Selecionada a OB", lista)

            if lista == 820:

                print("Funionarios da OB0820: ")
                    
                equipamentos_OB0820 = { "EQ0001" : "Onibus",
                                        "EQ0002" : "Automovel",
                                        "EQ0003" : "Vibro-acabadora",
                                        "EQ0004" : "Rolo chaoa",
                                        "EQ0005" : "Rolo pneu",
                                        "EQ0006" : "Rolo Conrrugado",
                                        "EQ0007" : "Automovel",
                                        "EQ0008" : "Rolo chapa",
                                        "EQ0009" : "Automovel"}
                
                lista_equipamentos_OB0820 = {"EQ0001", "EQ0002", "EQ0003", "EQ0004", "EQ0005", "EQ0006", "EQ0007", "EQ0008", "EQ0009"}
                
                chaves = equipamentos_OB0820.keys()
                valores = equipamentos_OB0820.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in equipamentos_OB0820.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    equipamento_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {equipamento_procurado} está na obra!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(equipamento_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_equipamentos_OB0820

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()
            
            elif lista == 821:

                print("Funionarios da OB0820: ")
                    
                equipamentos_OB0820 = { "EQ0001" : "Onibus",
                                        "EQ0002" : "Automovel",
                                        "EQ0003" : "Vibro-acabadora",
                                        "EQ0004" : "Rolo chaoa",
                                        "EQ0005" : "Rolo pneu",
                                        "EQ0006" : "Rolo Conrrugado",
                                        "EQ0007" : "Automovel",
                                        "EQ0008" : "Rolo chapa",
                                        "EQ0009" : "Automovel"}
                
                lista_equipamentos_OB0820 = {"EQ0001", "EQ0002", "EQ0003", "EQ0004", "EQ0005", "EQ0006", "EQ0007", "EQ0008", "EQ0009"}
                
                chaves = equipamentos_OB0820.keys()
                valores = equipamentos_OB0820.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in equipamentos_OB0820.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    equipamento_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {equipamento_procurado} está na obra!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(equipamento_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_equipamentos_OB0820.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()
            
            elif lista == 825:

                print("Funionarios da OB0820: ")
                    
                equipamentos_OB0825 = { "EQ0001" : "Onibus",
                                        "EQ0002" : "Automovel",
                                        "EQ0003" : "Vibro-acabadora",
                                        "EQ0004" : "Rolo chaoa",
                                        "EQ0005" : "Rolo pneu",
                                        "EQ0006" : "Rolo Conrrugado",
                                        "EQ0007" : "Automovel",
                                        "EQ0008" : "Rolo chapa",
                                        "EQ0009" : "Automovel"}
                
                lista_equipamentos_OB0825 = {"EQ0001", "EQ0002", "EQ0003", "EQ0004", "EQ0005", "EQ0006", "EQ0007", "EQ0008", "EQ0009"}
                
                chaves = equipamentos_OB0825.keys()
                valores = equipamentos_OB0825.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in equipamentos_OB0825.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    equipamento_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {equipamento_procurado} está na obra!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(equipamento_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_equipamentos_OB0825.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()

            elif lista == 826:

                print("Funionarios da OB0826: ")
                    
                equipamentos_OB0826 = { "EQ0001" : "Onibus",
                                        "EQ0002" : "Automovel",
                                        "EQ0003" : "Vibro-acabadora",
                                        "EQ0004" : "Rolo chaoa",
                                        "EQ0005" : "Rolo pneu",
                                        "EQ0006" : "Rolo Conrrugado",
                                        "EQ0007" : "Automovel",
                                        "EQ0008" : "Rolo chapa",
                                        "EQ0009" : "Automovel"}
                
                lista_equipamentos_OB0826 = {"EQ0001", "EQ0002", "EQ0003", "EQ0004", "EQ0005", "EQ0006", "EQ0007", "EQ0008", "EQ0009"}
                
                chaves = equipamentos_OB0826.keys()
                valores = equipamentos_OB0826.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in equipamentos_OB0826.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    equipamento_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {equipamento_procurado} está na obra!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(equipamento_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_equipamentos_OB0826.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()

            elif lista == 794:

                print("Funionarios da OB0794: ")
                    
                equipamentos_OB0794 = { "EQ0001" : "Onibus",
                                        "EQ0002" : "Automovel",
                                        "EQ0003" : "Vibro-acabadora",
                                        "EQ0004" : "Rolo chaoa",
                                        "EQ0005" : "Rolo pneu",
                                        "EQ0006" : "Rolo Conrrugado",
                                        "EQ0007" : "Automovel",
                                        "EQ0008" : "Rolo chapa",
                                        "EQ0009" : "Automovel"}
                
                lista_equipamentos_OB0794 = {"EQ0001", "EQ0002", "EQ0003", "EQ0004", "EQ0005", "EQ0006", "EQ0007", "EQ0008", "EQ0009"}
                
                chaves = equipamentos_OB0794.keys()
                valores = equipamentos_OB0794.values()
                
                i = 1
                
                # Apresentando os funcionarios 
                for chaves, valores in equipamentos_OB0794.items():
                
                    print(f'({i}) Funionario {chaves} com a função de {valores}')
                    i = i + 1
                    
                puxa_pausa()
                
                # Contador que irá controlar o while
                quantos = int(input("Quantos funcionarios você quer confirmar: "))
                contador = 1

                corrigidos = []

                while contador <= quantos:

                    equipamento_procurado = input("\nDigite qual funcionario você está procurando: ")
                    print(f'o funcionario {equipamento_procurado} está na obra!')

                    contador = contador + 1

                    # Aqui ele vai colcoar o funcionario corrigido na lista
                    corrigidos.append(equipamento_procurado)
                    
                puxa_pausa()
                    
                # Coloquei para cima para que ele possa fazer a diferença antes no corrigidos ficas vazio
                diferencas = lista_equipamentos_OB0794.difference(corrigidos)

                print("Esses funcionarios estão na obra e estão em sua equipe!")

                # Aqui ele vai ler
                def is_empty(corrigidos):
                    return len(corrigidos) == 0
                

                # Enquanto a lista não estiver vazia, ele desinfilerando
                while not is_empty(corrigidos):
                    print(corrigidos.pop(0), " Funcionario está certo")
                    
                puxa_pausa()
                
                print("Esses funcionarios estão avulsos na Obra")
                    
                for i in diferencas:
                    print(f'O funcionario {i} esta na obra mas não esta em sua equipe!')
                    
                print("\nTchau Brigaduu")

                puxa_pausa()
            else :

                print("Digite o indice de OB valido!")

        else:
            print("Digite uma opção valida!")

# FIM DO PROGRAMA PROPRIAMENTE DITO


# VERIFICAÇÃO DE SENHA

if senha == senha_certa:
    while True:
        tudo()
        
else : 
    print("Você digitou sua senha incorreta, para uma maior segurança precisamos que você responda uma pergunta!")
    numero_real = int(input("Qual o numero que seu fatorial é igual a 120: "))

    fatorial(numero_real)
    
    if numero_real == 5:
        print("\nPermissão concedida, reinicie o programa!")
        
    else :
        print("Tente novamente!")
