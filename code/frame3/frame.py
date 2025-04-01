from tkinter import ttk
import tkinter as tk

class Frame3(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.preset()

    def preset(self):
        infv = tk.StringVar(value="ссылка на GitHub: https://github.com/Morhonom/bimprex")
        info = tk.Entry(self, textvariable=infv, state='readonly')
        info.pack(fill="x" )