from tkinter import *


def convert():
    if miles_label["text"] == "Miles":
        miles = float(miles_entry.get())
        kilos = round(miles * 1.609)
        kilometers.config(text=kilos)
    else:
        kilos = float(miles_entry.get())
        miles = round(kilos / 1.609)
        kilometers.config(text=miles)


def swap():
    if miles_label["text"] == "Miles":
        miles_label.config(text="Kilometers")
        right_label.config(text="Miles")
    else:
        miles_label.config(text="Miles")
        right_label.config(text="Kilometers")


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(background="Light Gray", pady=10, padx=10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(background="Light Gray", padx=5, pady=5)

miles_entry = Entry(justify="center")
miles_entry.grid(column=1, row=0)
miles_entry.config(width=10)
miles_entry.insert(END, string="0")

left_label = Label(text="is equal to")
left_label.grid(column=0, row=1)
left_label.config(background="light gray", padx=5, pady=5)

kilometers = Label(text=0)
kilometers.config(background="light gray", padx=5, pady=5)
kilometers.grid(column=1, row=1)

button = Button(text="Calculate", command=convert)
button.config(padx=5, pady=5)
button.grid(column=1, row=3)

button_2 = Button(text="Swap", command=swap)
button_2.config(padx=5, pady=5)
button_2.grid(column=2, row=3)

right_label = Label(text="Kilometers")
right_label.config(background="light gray", padx=5, pady=5)
right_label.grid(column=2, row=1)

window.mainloop()
