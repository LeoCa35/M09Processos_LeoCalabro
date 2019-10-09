import random

for lista in range(100):
    lista = [random.randint(1,100)]

print(lista)


#Solucionador d'equacions de primer grau
class SolucionadorEcuacions:
    num1 = 0
    num2 = 0
    num3 = 0


    def __init__(self,ecuacion):

        self.ecuacion = ecuacion.split()
        self.a = self.ecuacion[0]
        self.operador = self.ecuacion[1]
        self.c = int(self.ecuacion[2])
        self.d = self.ecuacion[3]
        self.e = int(self.ecuacion[4])
        self.f = self.a[:-1]
        print("Part12 = " + self.a)
        print("Part1 =  " + self.a[:-1])
        print("Part2 = " + str(self.c))
        print("ExtreuOperador = " + self.operador)
        print("Part3 = " + str(self.e))

    def calcula(self):
        self.num1 = float(self.f)
        self.num2 = float(self.c)
        self.num3 = float(self.e)
        if self.operador=="+":
            resultado=(self.num3-self.num2) / self.num1
        else:
            resultado=(self.num3+self.num2) / self.num1
        return resultado
        # if self.operacio=="+":
        #    resultado=(self.c-self.b)/self.a
        #    print(self.a[:-1] +" " +self.d + " "+int(respuesta))

        #else:
        #    resultado=(self.c+self.b)/self.a

        #if self.operador == "-":
        #    respuesta = (self.c + self.e)/f


print(SolucionadorEcuacions("7x + 10 = 3").calcula())
