import math
from scipy import integrate
import numpy
import matplotlib.pyplot as plt
import threading

def getRent(ii, y, ND1 ,ND2,ND3):
    return (0.9 * y[ii] + 0.09 * y[ii]) / (0.003 * y[ii] + 0.004 * y[ii] + 0.003 * y[ii] + 0.0009 * ii + 0.01)

def solve(s):#return z
    global k_param
    k_param = s
    xkt = k_param[1]
    ND1 = 2.16
    ND2 = 8.66
    ND3 = xkt*100/42.6
    y0 = [ND1, ND2, ND3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # начальные
    TimeReaction = k_param[2]
    # options_ODE = odeset('InitialStep', 0.1, 'MaxStep', 10)
    # [t, y] = ode23s( @ dib, [0:1: TimeReaction], y0, options_ODE) # для
    time = numpy.linspace(0, TimeReaction, TimeReaction)
    r = integrate.ode(dib).set_integrator("dopri5")
    r.set_initial_value(y0, time)
    y = numpy.zeros((len(time), len(y0)))
    for i in range(0, time.size):
        y[i, :] = r.integrate(time[i])
    # if (k_param[3] == 0): # Рентабельность
    #     z = getRent(k_param[2], y, ND1, ND2, ND3)
    # if (k_param[3] == 1): #Output
    #     print(k_param, y)
    #     z = y[k_param[2]] # выход x5
    return y
def dib(t,y):# СДУ
    dy = [0 for i in range(0, 17)]
    w = [0 for i in range(0, 7)]

    # dy=zeros(17,1)
    # w=zeros(7,1)
    global k_param
    #for i=1:1:8
    k = []
    for i in range(0, 8):
        A,Ea = getAEa(i,k_param[1])
        k.append(getKonstant(k_param[0], math.exp(A), Ea))


    w[0]= k[0]*y[2]*y[0]
    w[1]= k[1]*y[1]*y[11]
    w[2]= k[2]*y[1]*y[11]-k[7]*y[10]*y[13]
    w[3]= k[3]*y[0]*y[13]
    w[4]= k[4]*y[0]*y[13]
    w[5]= k[5]*y[0]*y[12]
    w[6]= k[6]*y[9]*y[10]


    dy[0] = -w[0]-w[3]-w[4]-w[5]
    dy[1] = -w[1]-w[2]
    dy[2] = -w[0]
    dy[3] = w[5]+w[3]
    dy[4] = w[4]
    dy[5] = w[1]+w[3]
    dy[6] = w[6]
    dy[9] = w[3]+w[4]+w[5]-w[6]
    dy[10] = w[1]+w[2]-w[6]
    dy[11] = w[0]-w[1]-w[2]+w[6]
    dy[12] = w[1]-w[5]
    dy[13] = w[2]-w[3]-w[4]
    dy[15] = 4*w[0]
    dy[16] = w[0]
    return dy


def getKonstant(T, k0, Ea): #расчет констант по уравнению Аррениуса
  R = 0.002
  k_k = k0*math.exp(-Ea/(R*(T+273)))
  return k_k

def getAEa(NumK,xkt):
    if NumK == 0:
            A = -162500*xkt**3 + 14250*xkt**2 - 403.75*xkt + 26.475
            Ea = -183333*xkt**3 + 16500*xkt**2 - 476.67*xkt + 28.1
    if NumK == 1:
            A = -704.55*xkt**2 - 87.864*xkt + 14.428
            Ea = -2131.8*xkt**2 - 20.245*xkt + 9.9253
    if NumK == 2:
            A = 83333*xkt**3 - 5000*xkt**2 + 91.667*xkt + 18.7
            Ea =  -104167*xkt**3 + 6250*xkt**2 - 114.58*xkt + 12.125
    if NumK == 3:
            A = -1000000*xkt**3 + 86500*xkt**2 - 1889.2*xkt + 24.25
            Ea = 20000*xkt**3 - 1850*xkt**2 + 41.5*xkt + 14.75
    if NumK == 4:
            A = -545.45*xkt**2 + 12.364*xkt + 12.042
            Ea = -500*xkt**2 + 5*xkt + 5.8
    if NumK == 5:
            A = -220833*xkt**3 + 20250*xkt**2 - 452.92*xkt + 21.825
            Ea = -831.82*xkt**2 + 27.755*xkt + 19.895
    if NumK == 6:
            A = -29167*xkt**3 + 2250*xkt**2 - 47.083*xkt + 21.875
            Ea =  -4166.7*xkt**3 + 250*xkt**2 - 4.5833*xkt + 10.725
    if NumK == 7:
            A = 1000000*xkt**3 - 128000*xkt**2 + 2790*xkt + 2
            Ea = 1000000*xkt**3 - 119500*xkt**2 + 2605*xkt + 0.5
    return A,Ea

def main():
    a = 0.01
    b = 0.05
    c = 0.0001
    for i in range(0, int(b/a/c)):
        first_parametr = i*c
        for j in range(0, 220):
            set_solve = [200, first_parametr, j, 0]
            d = solve(set_solve)
main()