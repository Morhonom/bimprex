from tkinter import ttk
import tkinter as tk
import pathlib as pl
from PIL import ImageTk, Image
from PIL.ImageOps import scale

from .defaultAction import Rescale

class ActionFrame(ttk.Frame):
    def __init__(self, master, index):
        super().__init__(master, borderwidth=1, relief="solid")
        self.master = master
        self.index = index
        # for i in fields_number:
        button_up = ttk.Button(self, text="up")
        button_down = ttk.Button(self, text="down")
        button_delete = ttk.Button(self, text="delete", command=self.delete)
        button_up.pack(anchor="nw", side="left")
        button_down.pack(anchor="nw", side="left")
        button_delete.pack(anchor="nw", side="left")
    
    def delete(self):
        # self.master.packed_actions.pop(self.index)
        print(self.index, "||" , self, "||", self.master)
        print(self.master.preview_number)
        # self.master.update_actions(self.master)
        

class Frame2(ttk.Frame):
    def __init__(self, master, root_folder):
        super().__init__(master)
        self.root_folder = root_folder
        self.preview_number = 0
        self.packed_actions = []
        self.preset()

    def preset(self):
        

        self.frm1 = ttk.Frame(self, borderwidth=2, relief="solid")
        frm2 = ttk.Frame(self, borderwidth=2, relief="solid")
        self.frm1.pack_propagate(False)
        frm2.pack_propagate(False)
        self.frm1.pack(side="left", fill="both", expand=True)
        frm2.pack(side="left", fill="both", expand=True)
        # frm1.grid(column=0, row=0, sticky="nsew")
        # frm2.grid(column=1, row=0, sticky="nsew")

        self.frm4 = ttk.Frame(
            frm2, borderwidth=2, relief="solid", width=100, height=100
        )
        # self.frm4.pack_propagate(False)
        self.frm4.pack(anchor="s", side="bottom", fill="y")

        button_previus = ttk.Button(
            self.frm4, text="left", command=self.previos_preview
        )
        button_next = ttk.Button(self.frm4, text="right", command=self.next_preview)
        button_change = ttk.Button(self.frm4, text="change")
        button_previus.pack(anchor="sw", side="left")
        button_next.pack(anchor="sw", side="left")
        button_change.pack(anchor="sw", side="left")

        self.frm3 = ttk.Frame(frm2, borderwidth=2, relief="solid")
        self.frm3.pack(anchor="n", expand=True, fill="both")
        self.paths = []
        self.image_prev = ttk.Label(self.frm3)
        self.image_prev.pack()
        self.root_folder.trace("w", self.__on_root_folder_change)

        frm5 = ttk.Frame(self.frm1, borderwidth=2, relief="solid")
        frm5.pack(side="top")

        test_list = ["select action", "scale", "crop"]
        self.added_action = tk.StringVar()
        self.dropdown = ttk.OptionMenu(
            frm5,
            self.added_action,
            test_list[0],
            *test_list[1:],
            command=self.add_action,
        )
        self.dropdown.pack()
        
        self.frm6 = ttk.Frame(self.frm1, borderwidth=1, relief="solid")
        self.frm6.pack(expand=True, fill="both")

        self.bind("<<NotebookTabChanged>>", self.prev_redraw)
        self.bind("<Configure>", self.prev_redraw)

    def __on_root_folder_change(self, *args):
        self.paths = []

        for i in pl.Path(self.root_folder.get()).glob("*.*"):
            self.paths.append(i)
            # print(i)
        self.preview_image = Image.open(self.paths[0])
        self.image_prev.config(image=self.preview_image)

    def prev_redraw(self, *args):
        frame_width = self.frm3.winfo_width()
        frame_height = self.frm3.winfo_height()
        self.preview_image.size
        factor = min(
            frame_width / self.preview_image.size[0],
            frame_height / self.preview_image.size[1],
        )
        self.image = ImageTk.PhotoImage(scale(self.preview_image, factor))
        self.image_prev.config(image=self.image)
        print("fac")

    def next_preview(self):
        if self.preview_number + 1 < len(self.paths):
            self.preview_number += 1
            self.preview_image = Image.open(self.paths[self.preview_number])
            self.prev_redraw()

    def previos_preview(self):
        if self.preview_number - 1 >= 0:
            self.preview_number -= 1
            self.preview_image = Image.open(self.paths[self.preview_number])
            self.prev_redraw()

    def add_action(self, b):
        print("fack", b)
        index = len(self.packed_actions)
        self.packed_actions.append([Rescale()])
        self.packed_actions[-1].append(ActionFrame(self.frm6, index))
        for i in self.packed_actions:
            i[1].pack()
            # print(self.packed_actions)
        self.dropdown["text"]="penis"
        
    
    def update_actions(self, master):
        for i in master.packed_actions:
            i[1].pack()
            print(master.packed_actions)
        
        