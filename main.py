import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
card = {}


def card_ok():
    global data_dict
    data_dict.remove(card)
    data_to_learn = pandas.DataFrame(data=data_dict)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    random_card()


def random_card():
    global card, flip_time
    window.after_cancel(flip_time)
    card = random.choice(data_dict)
    card_widget.itemconfig(card_side, image=card_front)
    card_widget.itemconfig(lang, text="French")
    card_widget.itemconfig(word, text=card["French"])
    flip_time = window.after(3000, func=flip_card)


def flip_card():
    card_widget.itemconfig(card_side, image=card_back)
    card_widget.itemconfig(lang, text="English")
    card_widget.itemconfig(word, text=card["English"])


try:
    data = pandas.read_csv(filepath_or_buffer="data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")

data_dict = data.to_dict(orient="records")
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_time = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_widget = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = card_widget.create_image(400, 263, image=card_front)
card_widget.grid(row=0, column=0, columnspan=2)
lang = card_widget.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = card_widget.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

ok_image = PhotoImage(file="images/right.png")
ok_button = Button(image=ok_image, highlightthickness=0, borderwidth=0, command=card_ok)
ok_button.grid(row=1, column=1)

nok_image = PhotoImage(file="images/wrong.png")
nok_button = Button(image=nok_image, highlightthickness=0, borderwidth=0, command=random_card)
nok_button.grid(row=1, column=0)
random_card()

window.mainloop()
