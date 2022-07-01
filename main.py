
from textwrap import fill
from tkinter import *
from turtle import color
import math

from numpy import pad
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
mark = ""
timer = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="TIMER", fg=RED)
    canvas.itemconfig(canva_text, text= f"00:00")
    check_label.config(text = "") 
    global rep, mark
    rep = 0
    mark =""

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global rep 
    rep += 1

  
    check_label.config(text = mark) 

    if rep%8 ==0:
        count_down(LONG_BREAK_MIN)
        title_label.config(text="LONG BREAK", fg=RED)
    elif rep%2 == 0:
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(WORK_MIN)
        title_label.config(text="WORK", fg=GREEN)



def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count%60

     #dynamic typed
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canva_text, text= f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        global mark
        if rep%2 ==0:
            mark += "✓"  
        start_timer()
        
        



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro") 
window.config(padx=100, pady=50, bg=YELLOW)

#Label
title_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_pic)
canva_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Button
button_start = Button(text = "Start", command = start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)

#Button

    
button_restart = Button(text = "Reset",command = reset_timer, highlightthickness=0)
button_restart.grid(column=2, row=2)


#Label
check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
check_label.grid(column=1, row=3)



window.mainloop()