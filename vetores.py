'''
nomes = ["Nicolas", "Isablly", "Ana Gabriela", "Lucas", "Ingrid"]
idades = [19, 16, 17, 26, 19]

soma = 0

for idade in idades:
    soma += idade

media = soma/len(idades)

for i in range(len(idades)):
    if idades[i] > media:
        print("Aluno com maiores idades: ", nomes[i], " com a idade de", idades[i])
'''

nomes = []
idades = []

for i in range(5):
    nomes.append(input("Digite um nome: "))
    idades.append(int(input("Agora digite a idade dessas pessoas: ")))

print(nomes)
print(idades)

soma = 0

for idade in idades:
    soma += idade

media_idades = soma/len(idades)

for i in range(len(idades)):
    print(f"Esta pessoa {nomes[i]} tem a idade de {idades[i]}")
