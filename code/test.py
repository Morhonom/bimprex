import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("640x480")

frm1 = ttk.Frame(root, borderwidth=2, relief="solid")
frm2 = ttk.Frame(root, borderwidth=2, relief="solid")
frm1.pack_propagate(False)
frm2.pack_propagate(False)
frm1.pack(side="left", fill="both", expand=True)
frm2.pack(side="left", fill="both", expand=True)

test2 = ttk.Button(frm2, text="fasdf")
test2.pack(side="bottom")

root.mainloop()