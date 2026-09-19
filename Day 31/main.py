from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = []


# -------------------- LOAD DATA -------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")

    # If words_to_learn.csv exists but is empty
    if data.empty:
        original_data = pandas.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")

except (FileNotFoundError, pandas.errors.EmptyDataError):
    # If words_to_learn.csv does not exist
    # OR it is completely empty
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")


# -------------------- NEXT CARD -------------------- #

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(
        card_title,
        text="French",
        fill="black"
    )

    canvas.itemconfig(
        card_word,
        text=current_card["French"],
        fill="black"
    )

    canvas.itemconfig(
        card_background,
        image=card_front_image
    )

    flip_timer = window.after(
        3000,
        func=flip_card
    )


# -------------------- FLIP CARD -------------------- #

def flip_card():

    canvas.itemconfig(
        card_title,
        text="English",
        fill="white"
    )

    canvas.itemconfig(
        card_word,
        text=current_card["English"],
        fill="white"
    )

    canvas.itemconfig(
        card_background,
        image=card_back_image
    )


# -------------------- KNOWN WORD -------------------- #

def is_known():

    to_learn.remove(current_card)

    print(f"Words remaining: {len(to_learn)}")

    # Save remaining words
    data = pandas.DataFrame(to_learn)
    data.to_csv(
        "data/words_to_learn.csv",
        index=False
    )

    # Check if all words are completed
    if len(to_learn) == 0:

        window.after_cancel(flip_timer)

        canvas.itemconfig(
            card_title,
            text="Congratulations!",
            fill="black"
        )

        canvas.itemconfig(
            card_word,
            text="All Words Completed!",
            fill="black"
        )

        canvas.itemconfig(
            card_background,
            image=card_front_image
        )

        known_button.config(state="disabled")
        unknown_button.config(state="disabled")

    else:
        next_card()


# -------------------- UI -------------------- #

window = Tk()

window.title("Flashy")

window.config(
    bg=BACKGROUND_COLOR,
    padx=50,
    pady=50
)


# Timer
flip_timer = window.after(
    3000,
    func=flip_card
)


# Canvas
canvas = Canvas(
    width=800,
    height=526,
    highlightthickness=0,
    bg=BACKGROUND_COLOR
)


# Card Images
card_front_image = PhotoImage(
    file="images/card_front.png"
)

card_back_image = PhotoImage(
    file="images/card_back.png"
)


card_background = canvas.create_image(
    400,
    263,
    image=card_front_image
)


# Card Title
card_title = canvas.create_text(
    400,
    150,
    text="",
    font=("Arial", 40, "italic")
)


# Card Word
card_word = canvas.create_text(
    400,
    263,
    text="",
    font=("Arial", 60, "bold")
)


canvas.grid(
    row=0,
    column=0,
    columnspan=2
)


# -------------------- WRONG BUTTON -------------------- #

cross_image = PhotoImage(
    file="images/wrong.png"
)

unknown_button = Button(
    image=cross_image,
    highlightthickness=0,
    borderwidth=0,
    relief="flat",
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=next_card
)

unknown_button.grid(
    row=1,
    column=0
)


# -------------------- RIGHT BUTTON -------------------- #

check_image = PhotoImage(
    file="images/right.png"
)

known_button = Button(
    image=check_image,
    highlightthickness=0,
    borderwidth=0,
    relief="flat",
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    command=is_known
)

known_button.grid(
    row=1,
    column=1
)


# Show first card
next_card()


window.mainloop()