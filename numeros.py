#!/usr/bin/python3
from time import time
import random
import math
start_time = time()
seguir = True
N = 99989*100483
top = N**(0.5)
while seguir:
    a = 0
    c = True
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
    lon = len(l)
    g = []
    n = []
    f = []
    v = []
    gh = []
    ind = []
    for i in range(35):
        a = random.randint(0, int(top))+random.randint(0, 10)
        while a in n:
            a = random.randint(0, int(top))+random.randint(0, 10)
        b = (a**2)%N
        n.append(b)
        gh.append(a)
        #print(a, b)
    tot = []
    for num in n:
        t1 = [[num], [], []]
        tot.append(t1)
    #print(tot)
    dit = dict(zip(gh,tot))
    #print("***********ANTES DE FACTORIZAR***********")
    #print(dit)
    for key in dit.keys():
        f = []
        auxn = dit[key][0][0]
        for k in l:
            while dit[key][0][0] % k == 0 and dit[key][0][0] != 0:
                dit[key][0][0] = dit[key][0][0] // k
                f.append(k)
        if dit[key][0][0] != 1:
            f = []
        if len(f) == 0:
            ind.append(key)
            dit[key][1] = f
        else:
            g.append(f)
            dit[key][1] = f
            dit[key][0][0] = auxn
    #print("***********DESPUES DE FACTORIZAR*********")
    #for key in dit.keys():
    #    print(key,": ", end="")
    #    print(dit[key])
    #print("**********Los que no sirven*************")
    #print(ind)
    for i in ind:
        del dit[i]
    #print("purga")
    #for key in dit.keys():
    #    print(key,": ", end="")
    #    print(dit[key])
    for key in dit.keys():
        for yy  in l:
            cnt = 0
            for ii in dit[key][1]:
                if ii == yy:
                    cnt += 1
            dit[key][2].append(cnt)
    #print("************Con vectores************")
    #for key in dit.keys():
    #    print(key,": ", end="")
    #    print(dit[key])
    #print("***********combinaciones************")
    lkeys = list(dit.keys())
    total = len(dit.keys())
    for i in range(1, 2**total):
        nbin = str(bin(i))[2:]
        binstr = []
        suma = []
        par = True
        for l in range(lon):
            suma.append(0)
        for j in range(total - len(nbin)):
            binstr.append('0')
        for dig in nbin:
            binstr.append(dig)
        for p in range(total):
            if binstr[p] == '1':
                laux = dit[lkeys[p]][2]
                for ii in range(len(laux)):
                    suma[ii] = suma[ii] + laux[ii]
        for ij in suma:
            if ij % 2 != 0:
                par = False
        if par:
            #print("probando combinación: ", end="")
            #print(suma)
            x = 1
            y = 1
            for p in range(total):
                if binstr[p] == '1':
                    x = x * int(lkeys[p])
                    y = y * dit[lkeys[p]][0][0]
            x1 = (x**2) % N
            y1 = y % N
            if (x1 == y1):
                nump = math.gcd(x - y, N)
                if (nump != N and nump != 1):
                    print("{}={}*{}".format(N, N//nump, nump))
                    seguir = False
                    elapsed_time = time() - start_time
                    print("en {} segundos".format(elapsed_time))
                    break
