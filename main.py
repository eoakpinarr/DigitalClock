from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Saat')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background='black', foreground='magenta')
label.pack(anchor='center')
time()
mainloop()