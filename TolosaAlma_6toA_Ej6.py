#Ejercicio 6

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        if self.cantidad >= monto:
            self.cantidad -= monto

    def mostrar_total(self):
        print(self.nombre, "tiene", self.cantidad)


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Cliente 1")
        self.cliente2 = Cliente("Cliente 2")
        self.cliente3 = Cliente("Cliente 3")

    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(2000)
        self.cliente3.depositar(1500)

        self.cliente1.extraer(200)
        self.cliente2.extraer(500)

    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print("Total en el banco:", total)


banco = Banco()
banco.operar()
banco.cliente1.mostrar_total()
banco.cliente2.mostrar_total()
banco.cliente3.mostrar_total()
banco.deposito_total()