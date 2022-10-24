from tkinter import *

def miles_to_km():
    i = float(input.get())
    km = i * 1.609
    Output.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1,row=0)

#lables

my_lable_index = Label()
my_lable_index.grid(column=0,row=0)

my_lable = Label(text="is equal to")
my_lable.grid(column=0,row=1)

Label(text="Miles").grid(column=2, row=0)
Label(text="Km").grid(column=2, row=1)

Output = Label(text="0")
Output.grid(column=1,row=1)

#Button

button = Button(text="Calculate", command= miles_to_km)
button.grid(column=1,row=2)

window.mainloop()
