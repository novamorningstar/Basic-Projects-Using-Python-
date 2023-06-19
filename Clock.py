from tkinter import Label, Tk
import time
win = Tk()
win.title("Clock")
win.geometry("580x150")
win.resizable(1,1)
samp=("Bell Gothic Std Black", 68, 'bold')
bgc = "cyan2"
fgc = "crimson"
border_width = 25
l1 = Label(win, font=samp, bg=bgc, fg=fgc, bd=border_width)
l1.grid(row=0, column=1)
def clock():
    live = time.strftime("%I:%M:%S %p")
    l1.config(text=live)
    l1.after(200, clock)
clock()
win.mainloop()