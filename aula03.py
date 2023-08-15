'''
def primeiraFunao():      # Assinatura da função
    print("Minha primeira função! Que emoção!")

primeiraFunao()

# Parâmetros

def imprimeNome(nome):
    print(f"Nome: {nome}")

imprimeNome("Nicolas")

def monta_computador(CPU, armazenamento, memoria):
    print(f"A configuração é: \n \t - CPU: {CPU}, \n \t - Armazenamento: {armazenamento} \n \t - Memória: {memoria}Gb")

monta_computador("Intel Core i9", 1, 500)

# Função com retorno

def somaDoisValores(valor1, valor2):
    soma = valor1 + valor2

    return soma    # É oque vai se retornado

resultado = somaDoisValores(5, 9)
print("O valor da soma é: ", resultado)

# ============================================= DESAFIO =================================================

    def numeroInteiro(valor):
        soma = 0

        while (valor > 0):
            soma += valor
            valor -= 1

        return soma

print(numeroInteiro())

# De forma pratica ele vai, verificar se valor é igual a 0, não, vai jogar este valor digitado na soma
# E vai diminuir uma unidade no valor, e vai fazer novamente, mas agora valor vale 1 a menos
# Até valor ser 0, e a variavel soma tiver o conteudo de todas as somas

# ========================================================================================================

# ======================================== RECURSIVIDADE =================================================

# Resurvidade é chamar uma função dentro dela mesma.
# E preciso ter um caso base, quando a recursão ela termina de ser executada
# Caso base é o codigo, chamada recursiva é a parte que aparece a recursividade, tem que ter os dois

    def fatorial (numero):

        # CASO BASE
        if numero == 1:
            return 1

        # CHAMADA RECURSIVA
        return numero * fatorial(numero - 1)

    print(fatorial(int(input("Digite um numero: "))))

# Teste de mesa
# Fatorial de 3 = 3 * fatorial(2)
# Fatorial de 2 = 2 * fatorial(1)
# Fatorial de 1 = 1

# Basicamente ele vai chamar o resultado da função na propria função, como o IF não se cumpriu, continua o codigo
# Mas diminuindo 1 numero no valor inicial

# Tomar cuidado para não fazer um loop infinito, não satisfazendo o IF

# Traz mais performace para o codigo
# Faz o codigo ficar mais enchuto
# =========================================================================================================
'''

# ========================================= SOMAR RECURSIVO ===============================================

def somar(numero):
    # Precisa ter o caso base, a condição de parada do codigo
    if numero == 1:
        return 1

    # Chamada recursiva

    return numero + somar(numero - 1)

x = int(input("Informe um valor: "))
print("Soma", somar(x))

# Precisa-se sempre de um caso base e uma chamada recursiva

# ========================================================================================================

# ======================================= FIBONACCH RECURSIVO ============================================

def fibonacci (posicao):
    # Caso base
    if posicao == 0:
        return 0

    elif posicao == 1:
        return  1

    else :
        return fibonacci(posicao - 1) + fibonacci(posicao - 2)

# fibo(4) não cumpre os if, então: fibo(4) = fibo(3) + fibo(2)
#         Ele sempre vai fazer da direita para esquerda
# fibo(2) não cumpre os if, então: fibo(2) = fibo(1) + fibo(0)
#         Sempre da direita para esquerda
#         Tem que calcular 1 por 1
#         Cumpre a regra e reza


