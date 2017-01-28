def Calcular(m1, m50, m25, m10, m05):
    total = (m1 * 1) + (m50 * 0.5) + (m25 * 0.25) + (m10 * 0.10) + (m05 * 0.05)
    print("TOTAL NO COFRE EM R$ = ", total)

def Main():
    m1 = float(input("QUANT. DE MOEDAS DE R$ 1,00 = "))
    m50 = float(input("QUANT. DE MOEDAS DE R$ 0,50 = "))
    m25 = float(input("QUANT. DE MOEDAS DE R$ 0,25 = "))
    m10 = float(input("QUANT. DE MOEDAS DE R$ 0,10 = "))
    m05 = float(input("QUANT. DE MOEDAS DE R$ 0,05 = "))

    Calcular(m1, m50, m25, m10, m05)

Main()
