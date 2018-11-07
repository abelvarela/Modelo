from random import randint
from math import log


def mixto():
    c = float(input("Ingrese Constante Aditiva: "))
    a = float(input("Ingrese Constante Multiplicativa: "))
    m = float(input("Ingrese Modulo: "))
    sem = float(input("Ingrese Semilla: "))
    gu = []
    for i in range (0,100):
        res = ((sem * a) + c) % m
        sem = res
        gu.append(res/m)
    return gu

def exp(ex,u):
    return -ex * log(u)
    
def normal(m,d,u):
    sum = 0
    for i in range (0,12):
        sum = sum + u
    return d * (sum - 6) + m 

def uniforme(a,b,u):
    return a + (b - a) * u


gu = mixto()

t, m, d, a, b, i, j = 0, 7, 2, 6, 9, 0, 0
conTip1, conTip2, conTip3, llTrab, dur = 0, 0, 0, 0, 0
ocio, espera, tipo = 0, 0, ""
interLleg, durMax = 0, 0
ex, ex1 = 10, 15


while(t<480):

    j = j + 1

    u = gu[i]

    if (u < 0.5):
        tipo = "Tipo 1"
        i = i + 1
        dur = normal(m,d,gu[i]) + 2
        conTip1 = conTip1 + 1
    

    elif (u < 0.7):
        tipo = "Tipo 2"
        i = i + 1
        dur = exp(ex,gu[i]) + 2
        conTip2 = conTip2 + 1

    else:
        tipo = "Tipo 3"
        i = i + 1
        dur = uniforme(a,b,gu[i]) + 2
        conTip3 = conTip3 + 1

    i = i + 1
    llTrab = exp(ex1,gu[i])
    
    print("\n-------------------------------------------------------\n")

    if (dur == llTrab):
        #justo a tiempo
        print("En el trabajo N°"+str(j)+ " de " + tipo + " no hubo ocio ni espera.")
        t = t + dur

    elif (dur < llTrab):
        #ocio
        ocio = llTrab - dur
        print("En el trabajo N°"+str(j)+ " de " + tipo + " hubo "+str(ocio)+" minutos de ocio.")
        t = t + llTrab
    
    else:
        #espera
        espera = dur - llTrab
        print("En el trabajo N°"+str(j)+ " de " + tipo + " hubo "+str(espera)+" minutos de espera.")
        t = t + dur


    if (llTrab > interLleg):
        interLleg = llTrab
    
    if (dur > durMax):
        durMax = dur



print("\n-------------------------------------------------------\n")
print("Llgaron en total "+str(conTip1+conTip2+conTip3)+" trabajos.")
print("\n-------------------------------------------------------\n")
print("Llgaron en total "+str(conTip1)+" trabajos del tipo 1.")
print("Llgaron en total "+str(conTip2)+" trabajos del tipo 2.")
print("Llgaron en total "+str(conTip3)+" trabajos del tipo 3.")
print("\n-------------------------------------------------------\n")
print("El mayor intervalo entre llegadas es de "+str(interLleg))
print("\n-------------------------------------------------------\n")
print("El mayor tiempo de servicio es de "+str(durMax))
print("\n-------------------------------------------------------\n")