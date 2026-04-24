#Ejercicio 4

class Calculadora:
    def __init__(self):
        self.valor1= int(input("Ingrese el primer valor:"))
        self.valor2=int(input("Ingrese el segundo valor:"))

    def suma(self):
        self.suma=self.valor1+self.valor2
        print("La suma de los dos valores es igual a:",self.suma)

    def resta(self):
        self.resta=self.valor1-self.valor2
        print("La resta de los dos valores es igual a:",self.resta)
    
    def multiplicacion(self):
        self.mult=self.valor1*self.valor2
        print("La multiplicación entre ambos valores da como resultado:",self.mult)
    
    def division(self):
        self.div=self.valor1/self.valor2
        print("La división entre ambos valores es de:",self.div)

clase=Calculadora()

clase.suma()
clase.resta()
clase.multiplicacion()
clase.division()