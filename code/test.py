import tkinter as tk
from tkinter import ttk

class ActionFrame(ttk.Frame):
    def __init__(self):
        super().__init__(root, borderwidth=2, relief="solid")

root = tk.Tk()

root.geometry("640x480")

frm1 = ActionFrame()
a = []
for i in range(5):
    a.append(ttk.Button(frm1, text=1))
    a[-1].pack(anchor="sw")
frm1.pack(side="left", fill="x", expand=True)
root.mainloop()

