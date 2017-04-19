#09. Recebe um número inteiro e imprima na tela seu antecessor e o seu sucessor

def RecebeNumInt(n):
    antecessor = n - 1
    sucessor = n + 1

    return "ANTECESSOR: " + str(antecessor) + " ; SUCESSOR: " + str(sucessor)


num = int(input("DIGITE UM NUMERO: "))
print(RecebeNumInt(num))
