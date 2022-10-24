from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

my_lable = Label(text="I am a Lable", font=("Arial", 24, "bold"))
my_lable.pack()

#Button

def button_clicked():
    my_lable.config(text= input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()


window.mainloop()
