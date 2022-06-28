from tkinter import *
from PIL import ImageTk, Image

root=Tk()

canvas= Canvas(root, width= 600, height= 400)
canvas.pack()

img= (Image.open("4H.png"))

resized_image= img.resize((207,317), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

canvas.create_image(10,10, anchor=NW, image=new_image)

root.mainloop()