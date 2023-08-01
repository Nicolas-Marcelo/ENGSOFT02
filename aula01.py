'''
Operadores Aritmeticos
Adição  ->  +
Subtração  ->  -
Multiplicação  ->  *
Divisão  ->  /
Exponenciação/potencia  ->  **
parte inteira da divição  ->  //
Móculo da divisão  ->  %
(oque sobra da divição)
'''



#Entrada e Saída

print("Digite seu nome:")
nome = input()

print("Bem vindo(a), ", nome)



'''
Operadores de Comparação
==  ->  igualdade
!=  ->  Diferente
>  ->  Maior
>=  ->  Maior ou igual
<  ->  Menor
<=  ->  Menor ou igual
'''

#Estruturas Condicionais SImples


a = 6
b = 4
soma = a + b

if soma >= 10 :
    print("O valor da soma é: ", soma)

else :
    print("Valor falso do teste!")




'''
Operador Lógicos
AND  ->  e
(Todas as condições V para ser V
OR  0>  ou
(Todas condições F para ser F)
NOT  ->  não
(Negação da condição)
'''




x = 3.5
y = 1.2

if x < y and c > 3:
    print("As duas condições verdadeiras")
else:
    print("Pelo menos uma condição ou as duas são falsas")

# Estrutura condicional composta

temperatura = float(input("Informe a temperatura: "))

if temperatura >= 30 :
    print("Está muito calor!")

elif temperatura >= 24 :
    print("Está calor!")

elif temperatura >= 17 :
    print("A temperatura está Amena!")

elif temperatura >= 7 :
    print("A temperatura está fria!")

else :
    print("Muiro fria!")




# Validando numero se é par ou impar

numero = int(input("Informa um numero: "))

if numero % 2 == 0 and numero != 0:
    print(f'{numero} é par!')
elif numero % 2 != 0 :
    print(f'{numero} é impar!')
else:
    print(f'{numero} é zero!')



# Estruturas de repetição
# Variavel acumuladora

acumuladora = 0

for i in range(10) :
    nota1 = float(input("Informe a nota de numero um: "))
    nota2 = float(input("Informe a nota de numero dois: "))
    media = (nota1 + nota2) / 2

    print("A média do aluno é: {0:. 2f}".format(media))
    acumuladora = acumuladora + media

media_geral = acumuladora / 10

print(" A média da turma é: {0:.2f}".format(media_geral))








