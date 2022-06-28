from tkinter import *

# Definimos una función a ejecutar al clic el botón
def hola():
    print("Hola mundo!")

root = Tk()

# Enlezamos la función a la acción del botón
Button(root, text="Clícame", command=hola).pack()

root.mainloop() 