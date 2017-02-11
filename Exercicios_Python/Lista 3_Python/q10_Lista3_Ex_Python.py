'''
10. Escreva uma função que recebe a distância (em Km) e o tempo (em horas) de uma viagem, e retorne a
velocidade média da viagem.
'''

def VelocidadeMedia(distancia, tempo):
    vMedia = distancia / tempo

    return "Velocidade Média: " + str(vMedia) + " km/h"



distancia = int(input("DIGITE A DISTANCIA EM KM: "))
tempo = int(input("DIGITE O TEMPO EM HORAS: "))

print(VelocidadeMedia(distancia, tempo))
