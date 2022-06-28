import tkinter as tk
from tkinter import ttk
import random
from PIL import Image

class Panio: 
    manos = []
    mazo = []
    
    def __init__(self, cantidad_jugadores):
        for i in range(cantidad_jugadores):
            self.manos.append([])
        for i in range(1,14):
            for j in ['H','D','C','S']:
                self.mazo.append(str(i)+j+'.png')
                
    def sacar_carta(self):
        self.carta = self.mazo[random.randint(0,len(self.mazo)-1)]
        self.mazo.remove(self.carta)
        return self.carta
    
    def iniciar_juego(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1, width=1300, height=700, background="darkgreen")
        self.canvas1.grid(column=0, row=0)
        self.carta1 = tk.PhotoImage(file=self.manos[0][0])
        self.canvas1.create_image(500, 430, image=self.carta1, anchor="nw")
        self.carta2 = tk.PhotoImage(file=self.manos[0][1])
        self.canvas1.create_image(550, 430, image=self.carta2, anchor="nw")
        self.carta3 = tk.PhotoImage(file="red_back.png")
        self.canvas1.create_image(500, 20, image=self.carta3, anchor="nw")
        self.carta4 = tk.PhotoImage(file=self.manos[1][1])
        self.canvas1.create_image(550, 20, image=self.carta4, anchor="nw")
        self.carta5 = tk.PhotoImage(file="red_back.png")
        self.canvas1.create_image(900, 330, image=self.carta5, anchor="nw")
        self.carta6 = tk.PhotoImage(file="red_back.png")
        self.canvas1.create_image(950, 330, image=self.carta6, anchor="nw")
        self.carta7 = tk.PhotoImage(file="red_back.png")
        self.canvas1.create_image(100, 330, image=self.carta7, anchor="nw")
        self.carta8 = tk.PhotoImage(file="red_back.png")
        self.canvas1.create_image(150, 330, image=self.carta8, anchor="nw")
        self.ventana1.config(width=300, height=200)
        boton = ttk.Button(text="Pedir cartas")
        boton.place(x=400, y=550)
        self.ventana1.mainloop()
        
    def repartir(self, jugador):
        while len(self.manos[jugador]) < 2:
            self.carta = self.sacar_carta()
            if self.carta not in self.manos[jugador]:
                self.manos[jugador].append(self.carta)
        
p1 = Panio(4)
p1.repartir(0)
p1.repartir(1)
p1.repartir(2)
p1.repartir(3)

print(p1.manos)
p1.iniciar_juego()