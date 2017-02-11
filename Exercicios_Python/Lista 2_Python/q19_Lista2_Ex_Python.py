'''
19. Recebe a hora atual no formado HHMM e mostre quantos minutos passaram-se
desde início do dia.
'''

def Horas(hhmm):
    return hhmm // 100

def Minutos(hhmm):
    return str(hhmm % 100)

def TotalMinutos(hhmm):
    return (Horas(hhmm) * 60) + Minutos(hhmm)

def Difereca(hhmm1, hhmm2):
    min1 = TotalMinutos(hhmm1)
    min2 = TotalMinutos(hhmm2)

    return min1 - min2

hhmm = int(input("DIGITE A HORA NO FORMATO HHMM: "))

print("%dh %dmin = %d" % (Horas(hhmm), Minutos(hhmm), TotalMinutos(hhmm)))
