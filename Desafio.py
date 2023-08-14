# DESAFIO
def numeroInteiro(valor):
    soma = 0

    while (valor > 0):
        soma += valor
        valor -= 1

    return soma

print(numeroInteiro(10))

# De forma pratica ele vai, verificar se valor é igual a 0, não, vai jogar este valor digitado na soma
# E vai diminuir uma unidade no valor, e vai fazer novamente, mas agora valor vale 1 a menos
# Até valor ser 0, e a variavel soma tiver o conteudo de todas as somas 
