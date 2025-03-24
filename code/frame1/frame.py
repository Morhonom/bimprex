from tkinter import ttk, filedialog, PhotoImage
# import tkinter as tk
from typing import Callable
import pathlib as pl


class FolderSelector(ttk.Frame):
    def __init__(self, master, button_name: str, on_change_folder:Callable[[str], None]):
        super().__init__(master)
        self.on_change_folder = on_change_folder
        self.folder = ""
        button_ask_folder = ttk.Button(self, text=button_name, command=self.__select_folder)
        button_ask_folder.pack(anchor="w", side="left")
        self.path_info = ttk.Label(self, text="путь к папке", borderwidth=1, relief="solid")
        self.path_info.pack(fill="y", pady=3)
        
    def __select_folder(self):
        folder = filedialog.askdirectory()
        if folder != self.folder and folder:
            self.folder = folder
            self.on_change_folder(pl.Path(folder))
            self.path_info.config(text=folder)
            

class Gallery(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth=5, relief="solid")
        
    def gal_upd(self, pathh):
        self.nabee = []
        self.imga = []
        for i in pathh.iterdir():
            print(i)
            self.imga.append(PhotoImage(file=i))
            self.nabee.append(Gallery_img(self, self.imga[-1]))
            # self.imga.append(PhotoImage(file=i))
            # nabee.append(ttk.Label(self, image=self.imga[-1]))
            self.nabee[-1].pack(anchor="nw", side="left")

class Gallery_img(ttk.Label):
    def __init__(self, master, path_to_img):
        #self.img = PhotoImage(path_to_img)
        #print(type(self.img))
        super().__init__(master, borderwidth=1, relief="solid", image=path_to_img, width=100)
        

class Frame1(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.preset()

    def preset(self):
        self.galr = Gallery(self)
        self.input_folder = FolderSelector(self, "открыть папку", self.galr.gal_upd)
        self.input_folder.pack(anchor="nw")
        self.output_folder = FolderSelector(self, "папка выхода", print)
        self.output_folder.pack(anchor="nw")
        self.galr.pack(fill="both", side="bottom", expand=True)

        

    # def get_path_in(self):
