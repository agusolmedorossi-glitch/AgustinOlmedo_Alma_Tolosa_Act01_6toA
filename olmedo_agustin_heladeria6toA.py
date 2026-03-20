import tkinter as tk#la utilizaremos para usar herramientas de creacion de ventanas,botones,etc y la abreviamos como tk
from tkinter import messagebox#trae el uso de ventanas emergentes

sabores = {"Chocolate": (0, 0),"Vainilla": (0, 1),"Frutilla": (1, 0),"Dulce de leche": (1, 1),"Limón": (2, 0), "Maracuya": (2, 1), "granizado": (2,2), "menta granizada": (1,2), "chocolate dubai":(0,2)}
#puedes agregar sabores y poner su ubicacion en fila y columna
#usamos sabores como diccionario y valores son para el usarse como fila y columna
bochas = {1: 700, 2: 1200, 3: 1600}#guardamos el precio de cada bocha

total = 0
cantidad_bocha = 0
sabores_seleccionados = []
#utilizaremos estas 3 variables como globales para la entrada y salida de para actualizar los que eliga el cliente

#usamos for para recorrer los nombres de los sabores y usamos keys para mostrar el sabor
def mostrar_saboresDisp():
    lista = "Sabores disponibles:\n"
    for sabor in sabores.keys():
        lista = lista + "- " + sabor + "\n"
    messagebox.showinfo("Menú de Sabores", lista)

#recibe la cantidad de bochas y precio dependiendo el boton tocado
def registrar_bocha(cantidad, precio):
    global total, cantidad_bocha, sabores_seleccionados
    cantidad_bocha = cantidad
    total = precio
    sabores_seleccionados = []  
    total_label.config(text="Total a pagar: $" + str(total))
    info_label.config(text="Seleccionaste " + str(cantidad) + " bocha(s)")
    messagebox.showinfo("Tamaño", "Elegiste " + str(cantidad) + " bocha(s). ¡Ahora elegí los gustos!")

#primero aseguramos que el cliente eliga una cantidad de bochas y luego se agrega a la lista 
def seleccionar_sabor(nombre_helado):
    global sabores_seleccionados
    if cantidad_bocha == 0:
        messagebox.showwarning("Atención", "Primero tenés que elegir cuántas bochas querés")
        return
    if len(sabores_seleccionados) >= cantidad_bocha:
        messagebox.showwarning("Límite", "Ya elegiste los " + str(cantidad_bocha) + " sabores")
        return
    sabores_seleccionados.append(nombre_helado)
    info_label.config(text="Agregaste: " + nombre_helado)
    messagebox.showinfo("Sabor", "Sumaste el sabor: " + nombre_helado)

#verificamos que al consultar con el precio total no este vacio y si lo esta se informa
def calcular_precio():
    if total == 0:
        messagebox.showwarning("Vacío", "No hay nada para cobrar todavía")
    else:
        messagebox.showinfo("Precio", "El total es: $" + str(total))

#creamos un "ticket"  recorriendo la lista y mostrando con un for
def mostrar_resumen():
    if cantidad_bocha == 0 or len(sabores_seleccionados) == 0:
        messagebox.showwarning("Error", "El pedido no está terminado")
        return   
    texto_resumen = "RESUMEN DEL PEDIDO\n"
    texto_resumen = texto_resumen + "Bochas: " + str(cantidad_bocha) + "\n"
    texto_resumen = texto_resumen + "Sabores:\n"
    for s in sabores_seleccionados:
        texto_resumen = texto_resumen + " - " + s + "\n"
    texto_resumen = texto_resumen + "Precio final: $" + str(total)
    messagebox.showinfo("Ticket", texto_resumen)

def terminar_programa():
    if messagebox.askyesno("Salir", "¿Querés cerrar el programa?"):
        ventana.destroy()

#creamos una ventana con un tamaño y color
ventana = tk.Tk()
ventana.title("Heladería DULCE FRIO")
ventana.geometry("500x480")
ventana.configure(bg="beige")

#esto lo utilizamos para ordenar la fila de bochas a elegir
fila_bocha = 2

info_label = tk.Label(ventana, text="Elegí el tamaño para empezar", fg="blue", bg="beige")
info_label.grid(row=fila_bocha+1, column=0, columnspan=3, pady=5)

texto = tk.Label(ventana, text="--- Menú de Helados ---", font=("Arial", 20), fg="Black", bg="beige")
texto.grid(row=0, column=0, columnspan=3, pady=10)

boton1 = tk.Button(ventana, text="Mostrar sabores disponibles", bg="pink", fg="white", command=mostrar_saboresDisp)
boton1.grid(row=1, column=0, columnspan=3, pady=5)

#creamos cada boton con las keys del diccionario
#lambda verifica que se ejecute una accion cuando el boton se presiona
columna = 0
for cantidad, precio in bochas.items():
    boton = tk.Button(
        ventana, 
        text=str(cantidad) + " bocha(s) - $" + str(precio),
        command=lambda c=cantidad, p=precio: registrar_bocha(c, p)
    )
    boton.grid(row=fila_bocha, column=columna, padx=5, pady=5)
    columna += 1

total_label = tk.Label(ventana, text="Total a pagar: $0", font=("Arial", 12, "bold"), bg="beige")
total_label.grid(row=fila_bocha+2, column=0, columnspan=3, pady=5)

tk.Label(ventana, text="Seleccione sabores de helado:", fg="brown", bg="beige").grid(row=5, column=0, columnspan=3, pady=5)

#usando las coordenadas de sabores podemos ubicar cada boton de cada sabor
fila_base = 6
for sabor, (fila_offset, columna) in sabores.items():
    boton = tk.Button(
        ventana, 
        text=sabor, 
        width=20,
        command=lambda s=sabor: seleccionar_sabor(s)
    )
    boton.grid(row=fila_base + fila_offset, column=columna, padx=5, pady=5)

boton4 = tk.Button(ventana, text="Calcular el precio del pedido", bg="pink", fg="white", width=30, command=calcular_precio)
boton4.grid(row=9, column=0, columnspan=3, pady=5)

boton5 = tk.Button(ventana, text="Mostrar resumen final del pedido", bg="pink", fg="white", width=30, command=mostrar_resumen)
boton5.grid(row=10, column=0, columnspan=3, pady=5)

boton6 = tk.Button(ventana, text="Terminar programa", bg="orange", fg="white", width=30, command=terminar_programa)
boton6.grid(row=11, column=0, columnspan=3, pady=10)

#se encarga de mantener abierta la ventana
ventana.mainloop()