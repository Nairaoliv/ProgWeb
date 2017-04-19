def Calculo(total):
    tQueijo = total * (50 * 2)
    tPresunto = total * 50
    tCarne = total * (100)
    
    print("QUEIJO(kg) = ", tQueijo)
    print("PRESUNTO(kg) = ", tPresunto)
    print("CARNE(kg) = ", tCarne)

def Main():
    t = int(input("QUANT. SANDUICHES = "))

    Calculo(t)


Main()
