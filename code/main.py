import tkinter as tk
from tkinter import ttk


from frame1 import Frame1
from frame2 import Frame2
from frame3 import Frame3


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("bimprex")
        self.geometry("640x480")
        self.minsize(640, 480)
        # self.icon(default=".ico")
        self.root_folder = tk.StringVar(value="")
        self.root_folder_out = tk.StringVar(value="")
        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill="both")

        frame1 = Frame1(notebook, self.root_folder, self.root_folder_out)
        self.frame2 = Frame2(notebook, self.root_folder, self.root_folder_out)
        frame3 = Frame3(notebook)

        frame1.pack(expand=True, fill="both")
        self.frame2.pack(expand=True, fill="both")
        frame3.pack(expand=True, fill="both")

        notebook.add(frame1, text="входные данные")
        notebook.add(self.frame2, text="действия")
        notebook.add(frame3, text="инфо")

        self.root_folder.trace("w", self.bind_c)

    def bind_c(self, *args):
        self.bind("<<NotebookTabChanged>>", self.frame2.prev_redraw)


root = Root()


root.mainloop()
