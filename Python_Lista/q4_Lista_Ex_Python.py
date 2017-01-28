def Calculo(total):
    tQueijo = total * (50 * 0.001)
    tPresunto = tQueijo
    tCarne = total * (100 * 0.001)
    
    print("QUEIJO(kg) = ", tQueijo)
    print("PRESUNTO(kg) = ", tPresunto)
    print("CARNE(kg) = ", tCarne)

def Main():
    t = int(input("QUANT. SANDUICHES = "))

    Calculo(t)


Main()
