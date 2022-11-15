import tkinter as Blackjack21
from tkinter import ttk
import random
import socket
from PIL import Image

listacartas = ["img/1C.png", "img/1D.png", "img/1H.png", "img/1S.png", "img/2C.png", "img/2D.png", "img/2H.png",
               "img/2S.png", "img/3C.png", "img/3D.png", "img/3H.png", "img/3S.png", "img/4C.png", "img/4D.png",
               "img/4H.png", "img/4S.png", "img/5C.png", "img/5D.png", "img/5H.png", "img/5S.png", "img/6C.png",
               "img/6D.png", "img/6H.png", "img/6S.png", "img/7C.png", "img/7D.png", "img/7H.png", "img/7S.png",
               "img/8C.png", "img/8D.png", "img/8H.png", "img/8S.png", "img/9C.png", "img/9D.png", "img/9H.png",
               "img/9S.png", "img/10C.png", "img/10D.png", "img/10H.png", "img/10S.png", "img/11C.png", "img/11D.png",
               "img/11H.png", "img/11S.png", "img/12C.png", "img/12D.png", "img/12H.png", "img/12S.png", "img/13C.png",
               "img/13D.png", "img/13H.png", "img/13S.png"]

valores_cartas= {'img/1C.png':1 , 'img/1D.png':1 ,'img/1H.png':1 ,'img/1S.png':1 ,'img/2C.png':2, 'img/2D.png':2,
                 'img/2H.png':2, 'img/2S.png':2 , 'img/3C.png':3, 'img/3D.png':3, 'img/3H.png':3, 'img/3S.png':3,
                 'img/4C.png':4, 'img/4D.png':4,'img/4H.png':4, 'img/4S.png':4, 'img/5C.png':5, 'img/5D.png':5,
                 'img/5H.png':5,'img/5S.png':5,'img/6C.png':6,'img/6D.png':6, 'img/6H.png':6, 'img/6S.png':6, 'img/7C.png':7,
                 'img/7D.png':7, 'img/7H.png':7,'img/7S.png':7,'img/8C.png':8, 'img/8D.png':8, 'img/8H.png':8, 'img/8S.png':8,
                 'img/9C.png':9, 'img/9D.png':9,'img/9H.png':9,'img/9S.png':9, 'img/10C.png':10, 'img/10D.png':10, 'img/10H.png':10,
                 'img/10S.png':10, 'img/11C.png':10,'img/11D.png':10,'img/11H.png':10, 'img/11S.png':10, 'img/12C.png':10, 'img/12D.png':10,
                 'img/12H.png':10, 'img/12S.png':10,'img/13C.png':10,'img/13D.png':10, 'img/13H.png':10, 'img/13S.png':10}

class Jugador:
    posicion = []
    nro = 0
    crup = False
    
class Panio: 
    manos = []
    mazo = []
    cant_jug = 3
    crup = 1
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
        print(self.carta)
        self.mazo.remove(self.carta)
        return self.carta
    
    def iniciar_juego(self):
        self.ventana2=Blackjack21.Tk()
        self.canvas1=Blackjack21.Canvas(self.ventana2, width=1400, height=1400, background="darkgreen")
        self.canvas1.grid(column=0, row=0)
        for i in range(self.cant_jug):
            self.carta1 = Blackjack21.PhotoImage(file=self.manos[i][0])
            if i == self.crup:
                self.carta1 = Blackjack21.PhotoImage(file="img/red_back.png")
            self.carta2 = Blackjack21.PhotoImage(file=self.manos[i][1])
            self.lista_cartas.append([self.carta1,self.carta2])
        for j in range(self.cant_jug):
            self.canvas1.create_image(self.posiciones[j][0], self.posiciones[j][1], image=self.lista_cartas[j][0], anchor="nw")
            self.canvas1.create_image(self.posiciones[j][0] + 50, self.posiciones[j][1], image=self.lista_cartas[j][1], anchor="nw")
        
        self.ventana2.config(width=300, height=200)
        boton = ttk.Button(text="Pedir cartas")
        boton.place(x=400, y=550)
        self.ventana2.mainloop()
        
    def repartir(self, jugador):
        while len(self.manos[jugador]) < 2:
            self.carta = self.sacar_carta()
            if self.carta not in self.manos[jugador]:
                self.manos[jugador].append(self.carta)

if __name__ == "__main__":
    cant_jug = 4
    p1 = Panio(cant_jug)
    for i in range(cant_jug):
        p1.repartir(i)
    
    p1.iniciar_juego()