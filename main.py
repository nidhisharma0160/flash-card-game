from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


# ---------------------------- reading data from CSV & flipping cards ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    front.itemconfig(card_title, text="French", fill="black")
    front.itemconfig(card_text, text=current_card['French'], fill="black")
    front.itemconfig(background, image=front_img)
    flip_timer = window.after(ms=3000, func=flip_card)
def flip_card():
    global current_card
    front.itemconfig(card_title, text="English", fill="white")
    front.itemconfig(card_text, text=current_card['English'], fill="white")
    front.itemconfig(background, image=back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
#window setup#
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(ms=3000, func=flip_card)

#canvas setup#
front = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
background = front.create_image(400, 263, image=front_img)
front.config(bg=BACKGROUND_COLOR)
card_title = front.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = front.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
next_card()
front.grid(row=0, column=0, columnspan=2)

#buttons
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, command=next_card, highlightthickness=0)
cross_button.grid(row=1, column=0)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=is_known, highlightthickness=0)
right_button.grid(row=1, column=1)


window.mainloop()

