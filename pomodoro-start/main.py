import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
MINT="#a3b18a"
PALE="#f7c59f"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
repo = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global repo#accesssing the global variable repo
    window.after_cancel(timer)#after the canceling the timer(count_down)
    label.config(text="Timer", fg=GREEN)#changing the text of label to timer
    canvas.itemconfig(timer_text, text="00:00")#reseting the time
    label_check.config(text="")#reseting the checked area
    repo = 0  # Reset session count

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repo
    repo += 1#increase repo after every count_down

    if repo % 8 == 0:#if the repo reaches at 8 then break time will be 20 mins
        count = LONG_BREAK_MIN * 60
        label.config(text="Long Break", fg=RED)
    elif repo % 2 == 0:#if the repo is in even then there will be short break
        count = SHORT_BREAK_MIN * 60
        label.config(text="Break", fg=PINK)
    else:#else the repo will be in odd which means it work time
        count = WORK_MIN * 60
        label.config(text="Work", fg=GREEN)
    count_down(count)#call the count_down function

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)#separtes the min in count
    count_sec = count % 60#separates the secs in count
    if count_min < 10:
        count_min = f"0{count_min}"#format it in min
    if count_sec < 10:
        count_sec = f"0{count_sec}"#format it in sec
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)#decrease the count after every call to count_down(1s)
    else:
        start_timer()#call start_timer
        marks = ""#initializa marks
        work_sessions = math.floor(repo / 2)#after every 2 work and short break sessions,1 check mark will appear below the button
        for _ in range(work_sessions):
            marks += "✔"#append the mark after every 2 sessions
        label_check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", command=start_timer,bg=MINT,fg="black")
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer, bg=MINT, fg="black")
button_reset.grid(column=2, row=2)

label_check = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
label_check.grid(column=1, row=3)

window.mainloop()
