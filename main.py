import tkinter
from cProfile import label
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# import time
#
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

window.after(1000,)

#canvas widget
canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100,130, text="00:00" , fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#timer label
timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

#button der kalder start
start_button = tkinter.Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

#Button der kalder reset
reset_button = tkinter.Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

#checkmark
check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
