#06. Recebe uma velocidade em km/h, retorne esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)
def RecebeVeloc(veloc):
    vm = int(veloc / 3.6)
    return "VELOCIDADE EM M/S: " + str(vm) + " m/s"



vKm = int(input("DIGITE A VELOCIDADE EM KM/H: "))
print(RecebeVeloc(vKm))
