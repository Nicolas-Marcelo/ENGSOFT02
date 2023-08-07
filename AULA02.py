# Primeiro criar a variavel acumuladora, começa com 0
acumuladora = 0

# Depois criar o for ou laço de repetição
for i in range(10):

    print("===========================================================================\n")
    nome = input("Digite seu nome: ")
    print("Você e o cliente de numero {} a receber desconto!\n".format(i))
    valor = float(input("Digite o valor da compra: "))

    # Verificar o valor da compra, maior ou menor
    if valor >= 1500 :
        desconto = valor * 0.2

    else :
        desconto = valor * 0.15

    # Mecher com a aculudora
    acumuladora += desconto

    print(f"Olá, {nome}. O valor original de sua compra é de R$ {valor},\no total de desconto será de R$ {desconto} \ne oo valor a pagar será {valor - desconto}"f"")
    print("===========================================================================\n")
