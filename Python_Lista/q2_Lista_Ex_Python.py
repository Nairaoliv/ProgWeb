def Calculo(peq, media, grande):
    tPeq = peq * 10
    tMedia = media * 12
    tGrande = grande * 15
    print("\nTOTAL DE P: ", tPeq)
    print("\nTOTAL DE M: ", tMedia)
    print("\nTOTAL DE G: ", tGrande)

def Main():
    p = float(input("QUANTIDADE DE CAMISAS P: "))
    m = float(input("QUANTIDADE DE CAMISAS M: "))
    g = float(input("QUANTIDADE DE CAMISAS G: "))
    
    Calculo(p, m, g)


Main()
