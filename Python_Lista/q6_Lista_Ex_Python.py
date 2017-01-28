def Calcular(total):
   pDireito = 4 
   pEsquerdo = 3.50 * 2
   total = total * (pDireito + pEsquerdo)
   print("TOTAL GASTO = R$", total)

def Main():
    ent = float(input("QUANTIDADE DE GALINHAS: "))
    
    Calcular(ent)


Main()
    
