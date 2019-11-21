import numpy as np
import time
import threading
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



axis_x = []
axis_y = []
axis_z = []

def f2(a, b):
    c = np.exp(np.sin(np.cos(a + b) - b)) ** (a - b)
    axis_z.append(c)
    axis_x.append(a)
    axis_y.append(b)
    return c

def_res_func = f2(0,0)

def stream1(f2):
    global mn1
    mn1 = def_res_func
    for a in np.arange(0, 5, 0.01):
        for b in np.arange(0, 10, 0.01):
            f = f2(a,b)
            if f < mn1:
                mn1 = f
                # print(str(mn1))
    return mn1


##############################
def stream2(f2):
    global mn2
    mn2 = def_res_func
    for a in np.arange(4, 10, 0.1):
        for b in np.arange(0, 10, 0.1):
            f = f2(a,b)
            if f < mn2:
                mn2 = f
                # print(str(mn2))
    return mn2


##############################
def stream3(f2):
    global mn3
    mn3 = def_res_func
    for a in np.arange(0, 5, 0.1):
        for b in np.arange(9, 20, 0.1):
            f = f2(a,b)
            if f < mn3:
                mn3 = f
                # print(str(mn3))
    return mn3


##############################
def stream4(f2):
    global mn4
    mn4 = def_res_func
    for a in np.arange(4, 10, 0.1):
        for b in np.arange(9, 20, 0.1):
            f = f2(a,b)
            if f < mn4:
                mn4 = f
                # print(str(mn4))
    return mn4

##############################
thread1 = threading.Thread(target=stream1, args=(f2,))
thread2 = threading.Thread(target=stream2, args=(f2,))
thread3 = threading.Thread(target=stream3, args=(f2,))
thread4 = threading.Thread(target=stream4, args=(f2,))
start = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

if mn1 > mn2:
    mnn = mn2
else:
    mnn = mn1

if mn3 > mn4:
    mnm = mn4
else:
    mnm = mn3

if mnn > mnm:
    mn = mnm
else:
    mn = mnn

def index_of(a,list):
    for i in range(0,len(list)):
        if list[i] == a:
            return i
    return -1

finish = time.time()
t = finish - start
print("%2.10f"%(mn))
print(t,' sec')



ax = plt.axes(projection='3d')
ax.scatter3D(axis_x, axis_y, axis_z, cmap='Greens')
plt.show()


plt.scatter(axis_x, axis_z)
plt.show()