from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from PIL.ImageOps import scale

import tkinter as tk
import pathlib as pl


class FolderSelector(ttk.Frame):
    def __init__(self, master, button_name: str, root_folder):
        super().__init__(master)
        self.root_folder = root_folder
        button_ask_folder = ttk.Button(
            self, text=button_name, command=self.__select_folder
        )
        button_ask_folder.pack(anchor="w", side="left")
        self.path_info = ttk.Label(
            self, text="путь к папке", borderwidth=1, relief="solid"
        )
        self.path_info.pack(fill="y", pady=3)
        self.root_folder.trace("w", self.change_txt)

    def __select_folder(self):
        folder = filedialog.askdirectory()
        if folder != self.root_folder.get() and folder:
            self.root_folder.set(folder)

    def change_txt(self, *args):
        self.path_info.config(text=self.root_folder.get())


class Gallery(ttk.Frame):
    def __init__(self, master, root_folder):
        super().__init__(master, borderwidth=5, relief="solid")
        self.img_size = (200, 200)
        self.root_folder = root_folder
        self.root_folder.trace("w", self.gal_upd)
        self.root_folder.trace("w", self.bind_c)

    def bind_c(self, *args):
        self.bind("<Configure>", self.redraw)

    def redraw(self, *args):
        columns = self.winfo_width() // self.img_size[0]
        for index, img in enumerate(self.images):
            img.grid(row=index // columns, column=index % columns)

    def gal_upd(self, *args):
        self.images: list[GalleryImg] = []
        folder_path = pl.Path(self.root_folder.get())

        for img_path in folder_path.glob("*.*"):
            self.images.append(GalleryImg(self, img_path))

        self.redraw()


class GalleryImg(tk.Label):
    def __init__(self, master, path_to_img):
        self.img = Image.open(path_to_img)
        fac = 200 / max(self.img.size)
        self.img = scale(self.img, fac)
        self.img = ImageTk.PhotoImage(self.img)
        super().__init__(
            master, borderwidth=1, relief="solid", image=self.img, width=200, height=200
        )


class Frame1(ttk.Frame):
    def __init__(self, master, root_folder, root_folder_out):
        super().__init__(master)
        self.root_folder = root_folder
        self.root_folder_out = root_folder_out
        self.preset()

    def preset(self):
        self.galr = Gallery(self, self.root_folder)
        self.input_folder = FolderSelector(self, "открыть папку", self.root_folder)
        self.input_folder.pack(anchor="nw")
        self.output_folder = FolderSelector(self, "папка выхода", self.root_folder_out)
        self.output_folder.pack(anchor="nw")
        self.galr.pack(fill="both", side="bottom", expand=True)
