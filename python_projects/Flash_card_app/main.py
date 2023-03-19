from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Data #

french_english_data_frame = pandas.read_csv("data/french_words.csv")
french_english_dict = french_english_data_frame.to_dict(orient="records")


def count_down(count):
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count-1)
        print(timer)
    else:
        choose_word()


def choose_word():
    count = 5
    word = random.choice(french_english_dict)
    french = word["French"]
    flash_card.itemconfig(flash_title, text="French")
    flash_card.itemconfig(flash_word, text=french)
    count_down(count)


# UI #

flash_card = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_flash = PhotoImage(file="images/card_front.png")
back_flash = PhotoImage(file="images/card_back.png")
flash_card.create_image(400, 263, image=front_flash)
flash_card.grid(column=0, row=0, columnspan=2)
flash_title = flash_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
flash_word = flash_card.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, background=BACKGROUND_COLOR, padx=50,
                          command=choose_word)
incorrect_button.grid(column=0, row=1)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, background=BACKGROUND_COLOR, padx=50,
                        command=choose_word)
correct_button.grid(column=1, row=1)

window.mainloop()
