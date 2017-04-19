#02. Recebe um valor em real (R$), retorna 70% deste valor.

def RetornaValor(num):
    num = num * 0.7
    return "70% do valor = " + str(num)

n = float(input("Digite um valor em R$: "))

print(RetornaValor(n))
