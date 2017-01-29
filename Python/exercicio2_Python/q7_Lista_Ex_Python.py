def Calcular(l,g1,g2):
    resultado =(l * 0.35)+(g1 * 0.6) + (g2 * 2)
    print("QUANT. LITROS COMPRADOS EM R$ = ", resultado)

def Main():
    lata = float(input("QUANT. LATA DE 350 ML = "))
    garrafa1 = float(input("QUANT. GARRAFA DE 600 ML = "))
    garrafa2 = float(input("QUANT. GARRAFA DE 2L = "))

    Calcular(lata, garrafa1, garrafa2)
    
    
Main()
