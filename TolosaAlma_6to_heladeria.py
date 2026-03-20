import tkinter as tk 

sabores=["Chocolate", "Vainilla", "Frutilla", "Dulce de leche", "Limón", "Maracuya"]
bochas={1: 700, 2: 1200, 3: 1600}
pedido=[]
precio_pedido=[]

def mostrar_saboresDisp():
    cuadro.delete("1.0", tk.END) #Borra desde el inicio hasta el final (fila 1, columna 0)
    cuadro.insert(tk.END, "Sabores disponibles:\n") #Imprime al final
    for i in sabores:
        cuadro.insert(tk.END, i + "\n")

def elegir_bochas():
    cuadro.delete("1.0", tk.END)
    cant_bochas = entrada.get()
    cant_bochas = int(cant_bochas)
    if cant_bochas in [1,2,3]:
        precio_bocha = bochas[cant_bochas]
        precio_pedido.append(precio_bocha)
        cuadro.insert(tk.END, "Precio agregado: " + str(precio_bocha) + "\n")
    else:
        cuadro.insert(tk.END, "Cantidad de bochas no disponibles.\n")

def seleccionar_sabor():
    cuadro.delete("1.0", tk.END)
    sabor = entrada2.get()
    sabor.capitalize()
    if sabor in sabores:
        pedido.append(sabor)
        cuadro.insert(tk.END, "Sabor agregado: " + sabor + "\n")
    else:
        cuadro.insert(tk.END, "El sabor no esta disponible.\n")

def calcular_precio():
    cuadro.delete("1.0", tk.END)
    suma_total = 0
    if precio_pedido:
        for i in precio_pedido:
            suma_total += i
        cuadro.insert(tk.END, "El precio del pedido es: " + str(suma_total) + "\n")
    else:
        cuadro.insert(tk.END, "No hay ningún pedido guardado.\n")

def mostrar_resumen():
    cuadro.delete("1.0", tk.END)
    
    if pedido:
        cuadro.insert(tk.END, "---Resumen final del pedido---\n")
        cuadro.insert(tk.END, "Sabores pedidos:\n")
        for i in pedido:
            cuadro.insert(tk.END, i + "\n")
    else:
        cuadro.insert(tk.END, "No hay ningún pedido guardado\n")

    if precio_pedido:
        suma_total = 0
        for i in precio_pedido:
            suma_total += i
        cuadro.insert(tk.END, "Precio final: " + str(suma_total) + "\n")

def terminar_programa():
    ventana.destroy()

ventana=tk.Tk()
ventana.configure(bg="beige") #Se configura el color de la ventana
ventana.geometry("500x400") #Tamaño de la ventana

#Se pone un cuadro de texto para reemplazar la ventana
cuadro=tk.Text(ventana, height=10, width=40)
cuadro.grid(row=7, column=0, columnspan=3)

texto=tk.Label(ventana,text="---Menú---",font=("Arial",20), fg="Brown", bg="beige")
texto.grid(row=0, column=0, columnspan=3, pady=10)

#Mostrar sabores
boton1=tk.Button(ventana,text="Mostrar sabores disponibles", bg="pink", fg="white", command=mostrar_saboresDisp)
boton1.grid(row=1, column=0, columnspan=3, pady=10)

#Cantidad de bochas
texto1=tk.Label(ventana,text="Cantidad bochas:",fg="brown", bg="beige")
texto1.grid(row=2, column=0, padx=5, pady=5)

entrada=tk.Entry(ventana)
entrada.grid(row=2, column=1, padx=5, pady=5)

boton2=tk.Button(ventana,text="Guardar", bg="pink", fg="white", command=elegir_bochas)
boton2.grid(row=2, column=2, padx=5, pady=5)

#Seleccionar sabor
texto3=tk.Label(ventana,text="Ingrese el sabor", fg="brown", bg="beige")
texto3.grid(row=3, column=0, padx=5, pady=5)

entrada2=tk.Entry(ventana)
entrada2.grid(row=3, column=1, padx=5, pady=5)

boton3=tk.Button(ventana,text="Guardar", bg="pink", fg="white", command=seleccionar_sabor)
boton3.grid(row=3, column=2, padx=5, pady=5)

#Calcular precio
boton4=tk.Button(ventana,text="Calcular precio", bg="pink", fg="white", command=calcular_precio)
boton4.grid(row=4, column=0, columnspan=3, pady=10)

#Mostrar resumen
boton5=tk.Button(ventana,text="Mostrar resumen", bg="pink", fg="white", command=mostrar_resumen)
boton5.grid(row=5, column=0, columnspan=3, pady=10)

#Terminar
boton6=tk.Button(ventana,text="Terminar programa", bg="orange", fg="white", command=terminar_programa)
boton6.grid(row=6, column=0, columnspan=3, pady=10)

ventana.mainloop()