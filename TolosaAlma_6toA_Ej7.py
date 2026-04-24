#Ejercicio 7

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)


class CajaAhorro(Cuenta):
    def mostrar(self):
        self.imprimir()


class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def calcular_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)
        print("Plazo:", self.plazo)
        print("Interés:", self.interes)
        print("Importe interés:", self.calcular_interes())


caja = CajaAhorro("Ana", 5000)
plazo = PlazoFijo("Luis", 10000, 30, 5)

caja.mostrar()
plazo.mostrar()