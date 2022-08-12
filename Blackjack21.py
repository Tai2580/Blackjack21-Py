import tkinter as Blackjack21
from tkinter import ttk
import random
from PIL import Image



class Jugador:
    posicion = []
    nro = 0
    crup = False
    

class Panio: 
    manos = []
    mazo = []
    cant_jug = 3
    crup = 2
    posiciones = [[500,400],[500, 20],[900,300],[100,300]]
    lista_cartas = []
    lista_jug = []
    
    def __init__(self, cantidad_jugadores=4):
        self.cant_jug = cantidad_jugadores
        for i in range(self.cant_jug):
            jugador = Jugador()
            jugador.posicion = self.posiciones[i]
            jugador.nro = i
            if self.crup == i:
                jugador.crup = True
            self.lista_jug.append(jugador)
        print(self.lista_jug)
        for i in range(cantidad_jugadores):
            self.manos.append([])
        for i in range(1,14):
            for j in ['H','D','C','S']:
                self.mazo.append('img/' + str(i) + j + '.png')
                
    def sacar_carta(self):
        self.carta = self.mazo[random.randint(0,len(self.mazo)-1)]
        self.mazo.remove(self.carta)
        return self.carta
    
    def iniciar_juego(self):
        self.ventana1=Blackjack21.Tk()
        self.canvas1=Blackjack21.Canvas(self.ventana1, width=1300, height=700, background="darkgreen")
        self.canvas1.grid(column=0, row=0)
        for i in range(self.cant_jug):
            self.carta1 = Blackjack21.PhotoImage(file=self.manos[i][0])
            if i == self.crup:
                self.carta1 = Blackjack21.PhotoImage(file="img/red_back.png")
            self.carta2 = Blackjack21.PhotoImage(file=self.manos[0][1])
            self.lista_cartas.append([self.carta1,self.carta2])
        for j in range(self.cant_jug):
            self.canvas1.create_image(self.posiciones[j][0], self.posiciones[j][1], image=self.lista_cartas[j][0], anchor="nw")
            self.canvas1.create_image(self.posiciones[j][0] + 50, self.posiciones[j][1], image=self.lista_cartas[j][1], anchor="nw")
        
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