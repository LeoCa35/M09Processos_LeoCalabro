# -*- coding: utf-8 -*-
import sys
import pdb


class llista_primers:
    """
    Consiste en pedir un numero y darte los primeros numeros
    primos hasta que la longitud de la array concida con el
    numero introducido

    >>> llista_primers(5).llista
    [2, 3, 5, 7, 11]
    >>> llista_primers(12).llista
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    >>> llista_primers(15).llista
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    #Si la longitud de la array es 0
    def __init__(self, n):
        """
        Pide un numero
        """
        self.n = n
        self.llista = []
        #Aqui se crea la array
        self.busca()
        #llamamos a la funcion
    def busca(self):
        """
        Aqui comprueba si la longitud de la array es igual al
        numero introducido y va aumentando valores hasta que
        tiene los numeros primos
        """
        if (len(self.llista) == 0):
            #Si la longitud de la array es 0
            self.llista.append(2)
            self.busca()
        elif (len(self.llista) < self.n):
            #Si la longitud de la array es menor al nuestro numero introducido
            trobat = False
            seguent = self.llista[-1]+1
            #A seguent le asignamos la ultima posicion que tiene valor de la array
            while not trobat:
                for i in self.llista:
                    #i equivale al numero que se encuntre de la posicion de la array
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()


if __name__ == '__main__':
    """
    Sustitye el main
    """
    import doctest
    """
    l = llista_primers(int(sys.argv[1]))
    print l.llista
    """
    doctest.testmod()
