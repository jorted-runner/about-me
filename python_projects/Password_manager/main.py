from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = pass_entry.get()
    word = password_generator()
    pyperclip.copy(word)
    if len(password) == 0:
        pass_entry.insert(END, word)
    else:
        pass_entry.delete(0, END)
        pass_entry.insert(END, word)


# ------------------------------ SAVE PASSWORD ---------------------------------- #

def save_info():
    email = email_entry.get()
    password = pass_entry.get()
    site = site_entry.get()
    if len(site) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_okay = messagebox.askokcancel(title=site, message=f"These are the details entered:\nEmail: {email}"
                                                             f"\nPassword: {password}\nIs it okay to save?")
        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{site} | {email} | {password}\n")
            pass_entry.delete(0, END)
            site_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(END, "dee5cinco@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, background="light gray")

canvas = Canvas(width=200, height=200, highlightthickness=0, background="light gray")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

site_label = Label(text="Website:", background="light gray")
site_label.grid(column=0, row=1)

site_entry = Entry(width=50)
site_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", background="light gray")
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.insert(END, "dee5cinco@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password:", background="light gray")
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=28)
pass_entry.grid(column=1, row=3)

pass_generate_button = Button(text="Generate Password", command=generate_password)
pass_generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=50, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
