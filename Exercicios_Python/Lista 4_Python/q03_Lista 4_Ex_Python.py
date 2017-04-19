'03. Imprimir os 100 primeiros números pares.'


def NumerosPares(quantidade):
    for i in range(quantidade):
        if i % 2 == 0:
            print(i, end = ' ')
            

NumerosPares(100)

