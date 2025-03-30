import tkinter as tk
from tkinter import ttk


root = tk.Tk()

root.geometry("640x480")
notebook = ttk.Notebook()
notebook.pack(expand=True, fill="both")
frm1 = ttk.Frame(notebook)
frm2 = ttk.Frame(notebook)

frm1.pack(expand=True, fill="both")
frm2.pack(expand=True, fill="both")

notebook.add(frm1, text="входные данные") 
notebook.add(frm2, text="действия")

mb = tk.Menubutton(frm2, text="condiments", relief=tk.RAISED)

mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = tk.IntVar()
ketchVar = tk.IntVar()
mb.menu.add_command(label="mayo", command=lambda: print("mayo"))
mb.menu.add_command(label="ketchup", command=lambda: print("ketchup"))
mb.pack()

root.mainloop()

