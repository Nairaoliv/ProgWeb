#01. O que será impresso pelos algoritmos a seguir:
def Mensagem():
    x = 10
    y = 1
    x -= 1
    y += 2
    x = x - 1
    y = y + 2
    x = x - 1
    y = y + 2
    return "x=" + str(x) + " e y=" + str(y)
print(Mensagem())

'''
Resposta:
x=7 e y=7
'''



def DemoFuncao(b):
    a = (b * 2)
    b = b + 5
    c = a - b
    return "a = %d;b = %d;c = %d" % (a, b, c)
print(DemoFuncao(0))
print(DemoFuncao(5))
print(DemoFuncao(10))
print(DemoFuncao(15))
print(DemoFuncao(20))

'''
Resposta:
a = 0;b = 5;c = -5
a = 10;b = 10;c = 0
a = 20;b = 15;c = 5
a = 30;b = 20;c = 10
a = 40;b = 25;c = 15
'''
