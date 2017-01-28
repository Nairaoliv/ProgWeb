def Calculo(pao, broa):
    tPao = 0.12 * pao
    tBroa = 1.50 * broa
    total = tPao + tBroa
    poup = 0.1 * total
    print("TOTAL ARRECADADO DE PAES(R$)= ", round(tPao,2), "\nTOTAL ARRECADADO DE BROAS (R$)= ", round(tBroa, 2))
    print("TOTAL ARRECADADO (PAO + BROA) = R$", total)
    print("POUPANCA = ", round(poup,2))
    

def Main():
    p = float(input("QUANTIDADE DE PAES: "))
    b = float(input("QUANTIDADE DE BROAS: "))

    Calculo(p, b)


Main()
