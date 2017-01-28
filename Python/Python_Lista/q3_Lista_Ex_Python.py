def Calculo(valorTotal):
    t = valorTotal / 3

    c = round(t)
    a = round(t)
    f = round(t, 2)

    print("CARLOS = ", c, ", ", "ANDRE = ", a, ", ", "FELIPE = ", f)

def Main():
    vTotal = float(input("VALOR TOTAL DA CONTA (R$): "))

    Calculo(vTotal)
    
Main()

              
