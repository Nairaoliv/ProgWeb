#13. Escreva uma função que retorne “verdadeiro” se um número recebido for par e divisível por 3.

def RetornaValor(numero):
    if (numero % 2 == 0) and (numero % 3 == 0):
        return "\nVerdadeiro\n"
    else:
        return "\nFalso\n"

numero = int(input("DIGITE UM NÚMERO: "))
print(RetornaValor(numero)) 
