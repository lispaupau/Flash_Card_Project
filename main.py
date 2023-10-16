import tkinter
import pandas
import random
from tkinter import PhotoImage

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=back_img)


def is_know():
    to_learn.remove(current_card)
    print(len(to_learn))
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# Images
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
right_butt_img = PhotoImage(file='images/right.png')
wrong_butt_img = PhotoImage(file='images/wrong.png')

canvas = tkinter.Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
canvas.grid(column=0, row=0)
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0)

# Buttons
right_butt = tkinter.Button(image=right_butt_img, highlightthickness=0, command=is_know)
right_butt.grid(column=1, row=1)

wrong_butt = tkinter.Button(image=wrong_butt_img, highlightthickness=0, command=next_card)
wrong_butt.grid(column=0, row=1)

next_card()

window.mainloop()
