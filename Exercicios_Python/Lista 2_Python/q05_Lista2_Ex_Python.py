#05. Recebe uma velocidade em m/s, retorne esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

def RecebeVeloc(vm):
    vkm = vm * 3.6
    return "VELOCIDADE EM KM/H: " + str(vkm) + " km/h"



vm = int(input("DIGITE A VELOCIDADE EM M/S: "))
print(RecebeVeloc(vm))
