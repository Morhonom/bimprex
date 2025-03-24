import tkinter as tk
from tkinter import ttk
from frame1 import Frame1
from frame2 import Frame2
from frame3 import Frame3

root = tk.Tk()     # создаем корневой объект - окно
root.title("bimprex")     # устанавливаем заголовок окна
root.geometry("640x480")    # устанавливаем размеры окна
#root.iconbitmap(default="favicon.ico") # иконка
notebook = ttk.Notebook()
notebook.pack(expand=True, fill="both")

frame1 = Frame1(notebook)
frame2 = Frame2(notebook)
frame3 = Frame3(notebook)

frame1.pack(expand=True, fill="both")
frame2.pack(expand=True, fill="both")
frame3.pack(expand=True, fill="both")

notebook.add(frame1, text="входные данные")
notebook.add(frame2, text="действия")
notebook.add(frame3, text="инфо")



root.mainloop()