'''1. Faça uma função que recebe uma quantidade desejada de itens e retorna uma
lista carregada com essa quantidade. Faça outra função para exibir esses itens
esperados por espaço em branco.'''

def ListaQuant(quant):
    L = [12, 9, 5]
    i = 0

    while i < 3:
        print(len(L[quant]))
        break
    
            


quant = int(input("Número : "))
ListaQuant(quant)
