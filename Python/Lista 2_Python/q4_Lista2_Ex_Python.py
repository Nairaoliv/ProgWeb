#04. Recebe um valor em minutos, retorna o equivalente em horas e minutos.
def RecebeValorMin(valor):
    inteiro = int(valor / 60)
    resto = valor % 60
    return "VALOR EM HORAS: " + str(inteiro) + " horas " + str(resto) + " minutos"


v = int(input("DIGITE UM VALOR EM MINUTOS: "))

print(RecebeValorMin(v))
