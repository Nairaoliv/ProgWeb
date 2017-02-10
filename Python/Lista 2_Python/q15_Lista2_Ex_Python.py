'''
15. Recebe um número no formato CDU e imprima na forma UDC. Exemplo: 123, sairá 321. O número deve ser armazenado em
outra variável antes de ser impresso.
'''

def udc(cdu):
    u = cdu % 10
    cdu = cdu // 10
    d = cdu % 10
    cdu = cdu // 10
    c = cdu % 10
    
    return "UDC = " + str((u * 100) + (d * 10) + c)

num = int(input("DIGITE UM NUMERO: "))
print(udc(num))
