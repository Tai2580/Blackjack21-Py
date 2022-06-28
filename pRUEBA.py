import tkinter as tk
from tkinter import ttk
import random
from PIL import Image

lista_cartas = []
for i in range(1,14):
    for j in ['H','D','C','S']:
        lista_cartas.append(str(i)+j+'.png')


mano = []
while len(mano) < 2:
    carta = lista_cartas[random.randint(0,51)]
    if carta not in mano:
        mano.append(carta)

class cartas:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=1300, height=700, background="green")
        self.canvas1.grid(column=0, row=0)
        carta1=tk.PhotoImage(file=mano[0])
        self.canvas1.create_image(500, 430, image=carta1, anchor="nw")
        carta2=tk.PhotoImage(file=mano[1])
        self.canvas1.create_image(550, 430, image=carta2, anchor="nw")
        
    def cartasuma():
        carta3=tk.PhotoImage(file=mano[3])
        self.canvas1.create_image(600, 430, image=carta3, anchor="nw")
        
        self.ventana1.config(width=300, height=200)
        boton = ttk.Button(text="Pedir cartas")
        boton.place(x=400, y=550)
    
        Button(self.ventana1, text="Pedir cartas", command=cartasuma).pack()
    
        self.ventana1.mainloop()
        
    
       
cartas1=cartas()