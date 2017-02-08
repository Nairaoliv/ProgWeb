#4. Faça uma função que recebe três números por parâmetro e imprime na tela em ordem crescente.

def FuncaoCrescente(n1, n2, n3):
    valor = 0
    
    if (n1 < n2) and (n1 < n3):
        if(n2 < n3):
            return print(n1, n2, n3)
        else:
            return print(n1, n3, n2)
            
    elif(n2 < n1) and (n2 < n3):
        if(n1 < n3):
            return print(n2, n1, n3)
        else:
            return print(n2, n3, n1)
    else:
        if(n1 < n2):
            return print(n3, n1, n2)
        else:
            return print(n3, n2, n1)
    return 0
    
   
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))


print(FuncaoCrescente(num1, num2, num3))

