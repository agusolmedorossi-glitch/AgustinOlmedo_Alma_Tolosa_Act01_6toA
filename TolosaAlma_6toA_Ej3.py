#Ejercicio 3
class Triangulo():
    def __init__(self):
        self.lado1=int(input("Ingrese la medida del lado A:"))
        self.lado2=int(input("Ingrese la medida del ldo B:"))
        self.lado3=int(input("Ingrese la medida del ldo C:"))
    
    def tipo_triangulo(self):
        if self.lado1==self.lado2 and self.lado2==self.lado3:
            print("El triangulo con las medidas:",self.lado1,self.lado2,self.lado3,"es un triangulo equilatero.")

        elif self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3:
            print("El triangulo con las medidas:",self.lado1,self.lado2,self.lado3,"es un triangulo isoceles.")

        else:
            print("El triangulo con las medidas:",self.lado1,self.lado2,self.lado3,"es un triangulo escaleno")

clase=Triangulo()
clase.tipo_triangulo()