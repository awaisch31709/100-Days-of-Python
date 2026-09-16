from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global timer

    # Stop the running countdown
    if timer is not None:
        window.after_cancel(timer)

    # Reset everything
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")

    reps = 0
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    reps += 1
    print(f"reps: {reps}")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # 8th rep = long break
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    # 2nd, 4th, 6th rep = short break
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    # 1st, 3rd, 5th, 7th rep = work
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Add 0 before seconds below 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(
        timer_text,
        text=f"{count_min}:{count_sec}"
    )

    if count > 0:
        timer = window.after(
            1000,
            count_down,
            count - 1
        )

    else:
        start_timer()

        marks = ""
        work_sessions = math.floor(reps / 2)

        for _ in range(work_sessions):
            marks += "✔"

        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(
    padx=100,
    pady=50,
    bg=YELLOW
)


# Timer title
title_label = Label(
    text="Timer",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 50)
)

title_label.grid(
    row=0,
    column=1
)


# Tomato canvas
canvas = Canvas(
    width=200,
    height=224,
    bg=YELLOW,
    highlightthickness=0
)

tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(
    100,
    112,
    image=tomato_img
)

timer_text = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 35, "bold")
)

canvas.grid(
    row=1,
    column=1
)


# Start button
start_button = Button(
    text="Start",
    highlightthickness=0,
    command=start_timer
)

start_button.grid(
    row=2,
    column=0
)


# Reset button
reset_button = Button(
    text="Reset",
    highlightthickness=0,
    command=reset_timer
)

reset_button.grid(
    row=2,
    column=2
)


# Check marks
check_marks = Label(
    text="",
    fg=GREEN,
    bg=YELLOW,
    font=(FONT_NAME, 15)
)

check_marks.grid(
    row=3,
    column=1
)


window.mainloop()