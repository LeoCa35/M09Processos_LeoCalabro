#-*- coding: utf8 -*-
#4523

# 40 / 2 = 20
# 40 / 4 = 10
from datetime import datetime
from multiprocessing import Pool

def primers(num):
    #Hacemos un bucle el cual le pasamos un numero y va evaluando desde 2
    # hasta el numero, y calculamos si el número es primo o no
    for i in range(2, num/2):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':
    #Aqui seleccionamos el numero de processos que queremos que trabaje nuestro processador en esta tarea.
    pool = Pool(processes=8)
    l = range(40000000, 40000100)#[45445535, 56534563, 43566487, 43635453, 52346557, 53454433, 43546453, 26847357, 54577647]
    start = datetime.now()
    s = pool.imap(primers,l)
    #Aqui hacemos 2 bucles para separar cada proceso, uno para que printe el numero y otro para que te devuelva si el número es primo o no
    for i in l:
        for j in s:
            print(i,j)


    print datetime.now() - start

    """
    pool = Pool(processes=8): Aqui seleccionamos el numero de processos que queremos que trabaje nuestro processador en esta tarea.
    Sale mas a cuenta tener más processos si el ordenador solo hace 1 tarea, ya que se podran enfocar todos estos procesos en esta última.
    Si se utiliza el ordenador para mas de una tarea no saldria a cuenta ya que se veria afectada todas las otras aplicaciones debido a
    que tienes distintos processos activos en distintas aplicaciones.
    """
