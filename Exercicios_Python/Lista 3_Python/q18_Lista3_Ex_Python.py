#18. Crie uma função que recebe três valores inteiros e retorna o maior delas. Suponha não haver empates.

def RetornaMaior(n1, n2, n3):

    if(n1 > n2) and (n1 > n3):
        return "\nMaior: " + str(n1)
    elif(n2 > n1) and (n2 > n3):
        return "\nMaior: " + str(n2)
    elif(n3 > n1) and (n3 > n2):
        return "\nMaior: " + str(n3)
        

n1 = int(input("NUMERO 1: "))
n2 = int(input("NUMERO 2: "))
n3 = int(input("NUMERO 3: "))

print(RetornaMaior(n1, n2, n3))
