print("Bem vindo ao contagem de venda da padaria Sópão")

# Variaveis para resolução
pão = 0.80
brao = 2.50
euro = 4.60

# Perguntas para o usuario
quantos_pão = float(input("Quantos pães foram comprados? "))
quantos_broa = float(input("Quantas broas foram compradas? "))

# As operações logicas
valor_pão = (pão * quantos_pão)
valor_broa = (brao * quantos_broa)
valor_total = (valor_broa + valor_pão)

#Apresentação dos resultados
print("O valor total da compra é de: ", valor_total, "\n")

# Calculo das porcentagens e Mais aprensentação de resultados 
os_quarentap = 43%(valor_total)
print("Valor utilizado para custear gastos: ", round(os_quarentap, 3), "\n")

poupança = 15%(os_quarentap)
print("Valor depositado em poupança: ", round(poupança, 3), "\n")

euro = poupança / 4.60
print("Valor em euros a semrem comprados: ", round(euro, 3), "\n")





