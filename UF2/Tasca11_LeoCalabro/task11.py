# -*- coding: utf8 -*-
import md5
import random
import sys
from multiprocessing import Process, Semaphore

s = Semaphore(1)


def busca(x):
    
    f = open('fitxer.txt', 'r')
    fr = f.read()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    print fr[index+1:index2]
    f.close()
    


def substitueix(x):
    s.acquire()
    f = open('fitxer.txt', 'r')
    fr = f.read()
    f.close()
    index = fr.find('\n'+x+',')
    index2 = fr.find('\n', index+1)
    if index == -1:
        return 0
    print fr[index+1:index2]
    f = open('fitxer.txt', 'w')
    f.write(fr[:index+1])
    #Cambia la linea de index + 1 por la siguiente linea
    f.write(str(100) + ',' + md5.md5(str(100)).hexdigest() + "\n")
    f.write(fr[index2+1:])
    f.close()
    busca('100')
    s.release()


def inici():
    s.acquire()
    f = open('fitxer.txt', 'w')
    for i in range(100):
        f.write(str(i) + ',' + md5.md5(str(i)).hexdigest() + "\n")
    f.close()
    s.release()
    #print open('fitxer.txt', 'ro').read()


if __name__ == '__main__':

    inici()
    l = ['4', '10', '60']
    # for i in l:
    
    #p1 = Process(target=busca, args=('100',))
    p2 = Process(target=substitueix, args=['4', ])
    p3 = Process(target=substitueix, args=['10', ])
    p4 = Process(target=substitueix, args=['60', ])
    
    #p1.start()
    p2.start()
    p3.start()
    p4.start()
    # substitueix(i)
