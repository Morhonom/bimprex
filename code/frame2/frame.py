from tkinter import ttk, PhotoImage
import pathlib as pl
from PIL import ImageTk, Image


class Frame2(ttk.Frame):
    def __init__(self, master, root_folder):
        super().__init__(master)
        self.root_folder = root_folder
        self.preset()

    def preset(self):
        frm1 = ttk.Frame(self, borderwidth=2, relief="solid")
        frm2 = ttk.Frame(self, borderwidth=2, relief="solid")
        frm1.pack_propagate(False)
        frm2.pack_propagate(False)
        frm1.pack(side="left", fill="both", expand=True)
        frm2.pack(side="left", fill="both", expand=True)

        self.frm3 = ttk.Frame(frm2, borderwidth=2, relief="solid")
        self.frm3.pack(anchor="n", expand=True, fill="both")
        self.paths = []
        self.image_prev = ttk.Label(self.frm3)
        self.image_prev.pack()
        self.root_folder.trace("w", self.__on_root_folder_change)

        button_previus = ttk.Button(frm2, text="left")
        button_next = ttk.Button(frm2, text="right")
        button_change = ttk.Button(frm2, text="change")
        button_previus.pack(anchor="sw", side="left")
        button_next.pack(anchor="sw", side="left")
        button_change.pack(anchor="sw", side="left")
        
        self.bind("<<NotebookTabChanged>>", self.prev_redraw)

    def __on_root_folder_change(self, *args):
        for i in pl.Path(self.root_folder.get()).glob("*.*"):
            self.paths.append(i)
            # print(i)
        self.preveiw_image = Image.open(self.paths[0])
        self.image_prev.config(image=self.preveiw_image)
        
    def prev_redraw(self, *args):
        frame_width = self.frm3.winfo_width()
        frame_height = self.frm3.winfo_height()
        self.preveiw_image.size
        print(self.preveiw_image.size)
        print("fac")
