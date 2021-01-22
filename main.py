import tkinter
from tkinter import *

import tkinter as tk

window = tk.Tk()
window.geometry("1700x970")
window.resizable(False, False)
frame = tk.Canvas()
frame.config(width=1700, height=970)
frame.create_rectangle(0,1700,1900,900, fill='gray64')
frame['bg'] = 'gray20'
frame.pack()

window.mainloop()