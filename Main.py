from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(letters) for _ in range(nr_numbers)]

    password_list = password_letter + password_numbers + password_symbols
    random.shuffle(password_list)

    password_gen = "".join(password_list)
    global password
    password.insert(0, password_gen)
    pyperclip.copy(password_gen)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_e = website.get()
    email = email_user.get()
    password_e = password.get()
    if len(website_e) == 0 or len(email) == 0 or len(password_e) == 0:
        messagebox.showinfo(title= "Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_e, message=f"These are the details entered: \nEmail: {email}"
                           f"\nPassword: {password_e} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_e} | {email} | {password_e}\n")
                website.delete(0, END)
                password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row=0)

Label(text= "Website:").grid(column=0, row=1)
website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2)
website.focus()

Label(text= "Email/Username:").grid(column=0, row=2)
email_user = Entry(width=35)
email_user.grid(column=1, row=2, columnspan=2)
email_user.insert(0, "scienceloopyt@gmail.com")

Label(text= "Password: ").grid(column=0, row=3)
password = Entry(width=25)
password.grid(column=1, row=3, sticky=E)

generate_button = Button(text="Generate Password", command=gen_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command= save)
add_button.grid(column=1, row=4, columnspan=2, sticky=E)


window.mainloop()