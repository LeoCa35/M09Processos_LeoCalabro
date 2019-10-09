import random

for lista in range(100):
    lista = [random.randint(1,100)]

print(lista)


#Solucionador d'equacions de primer grau
class SolucionadorEcuacions:
    num1 = 0
    num2 = 0
    num3 = 0
    a = 0
    operador = ""
    c = 0
    d = 0
    e = 0
    f = 0


    def __init__(self,ecuacion):

        self.ecuacion = ecuacion.split()
        self.a = self.ecuacion[0]
        self.operador = self.ecuacion[1]
        self.c = float(self.ecuacion[2])
        print(self.c)
        print()
        self.d = self.ecuacion[3]
        self.e = float(self.ecuacion[4])
        self.f = self.a[:-1]
        """
        print("Part12 = " + self.a)
        print("Part1 =  " + self.a[:-1])
        print("Part2 = " + str(self.c))
        print("ExtreuOperador = " + self.operador)
        print("Part3 = " + str(self.e))
        """
    def calcula(self):
        self.num1 = float(self.f)
        self.num2 = float(self.c)
        self.num3 = float(self.e)
        try:
            if self.operador=="+":
                resultado=(self.num3-self.num2) / self.num1
                return resultado
        except:
            print("Suma Bien bro")

        try:
            if self.operador=="-":
                resultado=(self.num3+self.num2) / self.num1
                return resultado
        except Exception as e:
            print("Resta bien bro")

        try:
            if self.operador!="+":
                return self.operador
        except ValueError:
            print("Operador no valid: " + self.operador)

        try:
            if self.num2=="p":
                print("l'equacio conte caracter no calculables: ")
        except ValueError:
            return self.num2
        try:
            pass
        except Exception as e:
            raise
        # if self.operacio=="+":
        #    resultado=(self.c-self.b)/self.a
        #    print(self.a[:-1] +" " +self.d + " "+int(respuesta))

        #else:
        #    resultado=(self.c+self.b)/self.a

        #if self.operador == "-":
        #    respuesta = (self.c + self.e)/f


#print(SolucionadorEcuacions("7x + 10 = 3").calcula())
