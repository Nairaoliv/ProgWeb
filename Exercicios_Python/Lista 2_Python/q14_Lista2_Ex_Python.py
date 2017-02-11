'''
14. Recebe um número inteiro de 3 dígitos e mostre na tela o dígito da casa das dezenas.
'''

def CasaDezenas(cdu):
    u = cdu % 10
    cdu = cdu // 10
    d = cdu % 10
    cdu = cdu // 10
    c = cdu % 10
    
    return "DEZENA = " + str(d)

print(CasaDezenas(123))

