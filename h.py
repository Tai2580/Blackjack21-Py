import tkinter as Blackjack21
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