'04. Imprimir os múltiplos de 5, no intervalo de 1 até 500.'

def MultiplosCinco(n, m):

    for i in range (n, m+1):
        if i % 5 == 0:
            print(i, end = ' ')

MultiplosCinco(1, 500)

