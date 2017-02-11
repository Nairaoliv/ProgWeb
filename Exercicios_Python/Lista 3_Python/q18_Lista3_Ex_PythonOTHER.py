#18. Crie uma função que recebe três valores inteiros e retorna o maior delas. Suponha não haver empates.

def RetornaMaior(n1, n2, n3):

    valor = [n1, n2, n3]
    return "\nMaior valor: " + str(max(valor))
        

n1 = int(input("NUMERO 1: "))
n2 = int(input("NUMERO 2: "))
n3 = int(input("NUMERO 3: "))

print(RetornaMaior(n1, n2, n3))
