#07. Recebe 2 números, retorne a divisão da soma pela subtração dos números lidos.

def RecebeNum(n1, n2):
    soma = n1 + n2
    subtracao = n1 - n2
    divisao = round((soma / subtracao), 2)
    return "RESULTADO DA DIVISAO: " + str(divisao)
    

num1 = int(input("NUMERO 1: "))
num2 = int(input("NUMERO 2: "))

print(RecebeNum(num1, num2))
