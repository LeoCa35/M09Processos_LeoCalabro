import random

for lista in range(100):
    lista = [random.randint(1,100)]

print(lista)


#Solucionador d'equacions de primer grau
class SolucionadorEcuacions:

    def __init__(self,ecuacion):
        self.ecuacion = ecuacion.split()
        self.a = self.ecuacion[0]
        self.operador = self.ecuacion[1]
        self.c = int(self.ecuacion[2])
        self.d = self.ecuacion[3]
        self.e = int(self.ecuacion[4])
        print("Part12 = " + self.a)
        print("Part1 =  " + self.a[:-1])
        print("Part2 = " + self.c)
        print("ExtreuOperador = " + self.operador)
        print("Part3 = " + self.e)

    def calcula(self):
        if self.operador == "+":
            respuesta = (self.c - self.e)/self.a[:-1]

        if self.operador == "-":
            respuesta = (self.c + self.e)/self.a[:-1]

        print(self.a[:-1] +" " +self.d + " "+int(respuesta))







resultado = SolucionadorEcuacions("9x + 10 = 3").calcula()
