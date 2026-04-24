""""
class Alumno:
    def __init__(self):
        self.nombre=input("ingrese nombre del alumno: ")
        self.nota=int(input("ingrese nota del alumno: "))
    def mostrar(self):
        print(f"alumno: {self.nombre}")
        print(f"nota: {self.nota}")
    def mostrar_resultado(self):
        if self.nota >= 7:
            print(f"el alumno {self.nombre} a aprobado")
        else:
            print(f"el alumno {self.nombre} a desaprobado")
alumno= Alumno()
alumno.mostrar()
alumno.mostrar_resultado()
""""
""""
class Persona:
    def __init__(self):
        self.nombre=input("ingrese el nombre de la persona: ")
        self.edad=int(input("ingrese la edad de la persona: "))
    def mostrar(self):
        print(f"persona: {self.nombre}")
        print(f"edad: {self.edad}")
    def menor_mayor(self):
        if self.edad >= 18:
            print(f"la persona {self.nombre} es mayor de edad")
        else:
            print(f"la persona {self.nombre} es menor de edad")
persona=Persona()
persona.mostrar()
persona.menor_mayor()
""""
""""
class Triangulo:
    def __init__(self):
        self.lado1=float(input("ingrese el primer lado: "))
        self.lado2=float(input("ingrese el segundo lado: "))
        self.lado3=float(input("ingrese el tercer lado: "))
    def mayot(self):
        mayo= self.lado1
        if self.lado2>mayo:
            mayo=self.lado2
        if self.lado3>mayo:
            mayo=self.lado3
        print(f"el lado mayor es: {mayo}")
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("es un equilatero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("es un isoceles")
        else:
            print("es un escaleano")
triangulo=Triangulo()
triangulo.mayot()
triangulo.tipo_triangulo()
""""
""""
class Calculadora:
    def __init__(self):
        self.numero01=float(input("ingrese el primer nunmero: "))
        self.numero02=float(input("ingrese el segundo numero: "))
    def mostrar(self):
        print(f"numeros ingresados: {self.numero01} , {self.numero02}")
    def sumar(self):
        suma=self.numero01+self.numero02
        return print(f"{self.numero01} + {self.numero02}={suma}")
    def restar(self):
        resta=self.numero01-self.numero02
        return print(f"{self.numero01} - {self.numero02}={resta}")
    def multiplicacion(self):
        multi=self.numero01*self.numero02
        return print(f"{self.numero01} * {self.numero02}={multi}")
    def division(self):
        divi=self.numero01/self.numero02
        return print(f"{self.numero01} / {self.numero02}={divi}")
calculadora=Calculadora()
calculadora.mostrar()
calculadora.sumar()
calculadora.restar()
calculadora.multiplicacion()
calculadora.division()
""""
""""
class Agenda:
    def __init__(self):
        self.nombre=[]
        self.telefono=[]
        self.email=[]
    def administracion(self):
        op=0
        while True:
            print("1_añadir contacto")
            print("2_ lista de contactos")
            print("3_ buscar contacto")
            print("4_ editar contacto")
            print("5_ cerrar agenda")
            op=int(input("eliga una opcion: "))
            if op==1:
                self.contacto=input("ingrese nombre del contacto: ")
                self.nombre.append(self.contacto)
                self.numero=int(input("ingrese el numero del contacto: "))
                self.telefono.append(self.numero)
                self.gmail=input("ingrese el email del contacto: ")
                self.email.append(self.gmail)
            elif op==2:
                if len(self.nombre)==0:
                    print("no se a cargado nada aun...")
                else:
                    for i in range (len(self.nombre)):
                        print(f"nombre del contacto: {self.nombre[i]}")
                        print(f"telefono del contacto: {self.telefono[i]}")
                        print(f"email del contacto: {self.email[i]}")
            elif op==3:
                if len(self.nombre)==0:
                    print("no se a cargado nada aun...")
                else:
                    buscar=int(input("ingrese el numero del contacto: "))
                    print(f"contacto: {self.nombre[buscar]}, {self.telefono[buscar]}, {self.email[buscar]}")
            elif op==4:
                if len(self.nombre)==0:
                    print("no se a cargado nada aun...")
                else:
                    buscar=int(input("ingrese el numero del contacto: "))
                    self.reemplazonombre=input("ingrese nuevo nombre del contacto: ")
                    self.reemplazotelefono=input("ingrese nuevo telefono del contacto: ")
                    self.reemplazoemail=input("ingrese nuevo email del contacto: ")
                    self.nombre[buscar]=self.reemplazonombre
                    self.telefono[buscar]=self.reemplazotelefono
                    self.email[buscar]=self.reemplazoemail
            elif op==5:
                break
            else:print("opcion no existente")
agenda=Agenda()
agenda.administracion()
""""
""""
class Cliente:
    def __init__(self):
        self.nombre=input("ingrese nombre del cliente: ")
        self.cantidad=float(input("ingrese su cantidad de dinero: "))
    def depositar(self):
        monto=float(input(f"{self.nombre}ingrese la cantidad de dinero que depositara: "))
        self.cantidad = self.cantidad + monto
    def extraccion(self):
        monto=float(input(f"{self.nombre}ingrese la cantida de dinero que va a extraer"))
        if monto <= self.cantidad:
            self.cantidad = self.cantidad - monto # RESTA de la misma variable
        else:
            print("Saldo insuficiente")
    def mostrar_total(self):
       print(f"El cliente {self.nombre} tiene un saldo de: {self.cantidad}")
class Banco:
    def __init__(self):
        self.cliente1=Cliente()
        self.cliente2=Cliente()
    def operar(self):
        self.cliente1.depositar()
        self.cliente1.extraccion()
        self.cliente2.depositar()
        self.cliente2.extraccion()
    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad
        print(f"El total de dinero en el banco es: {total}")
        self.cliente1.mostrar_total()
        self.cliente2.mostrar_total()
banco=Banco()
banco.operar()
banco.deposito_total()
""""
""""
class Cuenta:
    def __init__(self):
        self.nombre=input("ingrese nombre del cliente: ")
        self.cantidad=float(input("ingrese la cantidad del cliente: "))
    def mostrar(self):
        print(f"titular: {self.nombre}, cantidad disponible: {self.cantidad}")
class caja_ahorro(Cuenta):
    def __init__(self):
        super().__init__()
    def mostrar_informacion(self):
        print("CAJA DE AHORRO")
        self.mostrar()
class plazo_fijo(Cuenta):
        def __init__(self):
            super().__init__()
            self.dias=int(input("ingrese la cantidad de dias: "))
            self.interes=float(input("ingrese el interes: "))
        def importe_interes(self):
             return self.cantidad*self.interes/100
        def mostrar_info(self):
             print("INFORMACION PLAZO")
             self.mostrar()
             print(f"plazo: {self.dias} dias ")
             print(f"interes: {self.interes}")
             print(f"total de intereses ganados: {self.importe_interes()}")
caja=caja_ahorro()
caja.mostrar_informacion()

plazo=plazo_fijo()
plazo.mostrar_info()
""""