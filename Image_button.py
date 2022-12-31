from tkinter import *
import PIL
from PIL import ImageTk, Image

count = 0

def click():
    global count
    count+=1
    print(count)

window = Tk()

load = Image.open("PicsArt_09-12-05.30.42.jpg")
photo = ImageTk.PhotoImage(load)

# = PhotoImage(file='giphy.gif')

button = Button(window,
                text="Draw A Card",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()
