import tkinter as tk
from tkinter import ttk
from frame1 import Frame1
from frame2 import Frame2
from frame3 import Frame3


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("bimprex")  # устанавливаем заголовок окна
        self.geometry("640x480")  # устанавливаем размеры окна
        self.minsize(640, 480)
        # self.iconbitmap(default="favicon.ico") # иконка
        self.root_folder = tk.StringVar(value="")
        self.root_folder_out = tk.StringVar(value="")
        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill="both")

        frame1 = Frame1(notebook, self.root_folder, self.root_folder_out)
        frame2 = Frame2(notebook, self.root_folder, self.root_folder_out)
        frame3 = Frame3(notebook)

        frame1.pack(expand=True, fill="both")
        frame2.pack(expand=True, fill="both")
        frame3.pack(expand=True, fill="both")
        
        self.bind("<<NotebookTabChanged>>", frame2.prev_redraw)

        notebook.add(frame1, text="входные данные") 
        notebook.add(frame2, text="действия")
        notebook.add(frame3, text="инфо")
        
    def asd(self, *args):
        print("fsdaf")


root = Root()


root.mainloop()
