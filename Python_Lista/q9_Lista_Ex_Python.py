def Calcular(sP, sU, aU):
    sResultado = sP / sU
    aPredio = sResultado * aU
    print("\nALTURA DO PREDIO EM METROS: ", round(aPredio, 2))
    

def Main():
    sPredio = float(input("INFORME TAMANHO DA SOMBRA DO PREDIO: "))
    sUsuario = float(input("INFORME TAMANHO DA SOMBRA DO USUARIO: "))
    aUsuario = float(input("INFORME ALTURA DO USUARIO: "))
    
    Calcular(sPredio, sUsuario, aUsuario)


Main()
s
