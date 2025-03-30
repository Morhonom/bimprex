from tkinter import ttk
import tkinter as tk
import pathlib as pl
from PIL import ImageTk, Image
from PIL.ImageOps import scale

from .defaultAction import Rescale


class ActionFrame(ttk.Frame):
    def __init__(self, master, class_var, delete_action, move_up, move_down):
        super().__init__(master, borderwidth=1, relief="solid")
        self.class_var = class_var
        self.fields = []
        self.fields_output = []
        self.master = master
        self.delete_action = delete_action
        self.move_up = move_up
        self.move_down = move_down
        button_up = ttk.Button(self, text="up", command=self.move_up_inside)
        button_down = ttk.Button(self, text="down", command=self.move_down_inside)
        button_delete = ttk.Button(
            self, text="delete", command=self.delete_action_inside
        )
        button_up.pack(anchor="nw", side="left")
        button_down.pack(anchor="nw", side="left")
        button_delete.pack(anchor="nw", side="left")

        for i in self.class_var.fields:
            print("adding fields")
            self.fields.append(ttk.Entry(self))
            self.fields_output.append(self.class_var.fields[i]["default_value"])
            self.fields[-1].pack()

        self.action = class_var()
        

    def delete_action_inside(self):
        self.delete_action(self)

    def move_up_inside(self):
        self.move_up(self)

    def move_down_inside(self):
        self.move_down(self)
        
    def update_fields_output(self):
        for i in range(len(self.fields)):
            self.fields_output[i] = self.fields[i].get()
        return self.fields_output


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
        button_change = ttk.Button(self.frm4, text="change", command=self.apply_actions_preview)
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
        
        self.frm6 = ttk.Frame(self.frm1, borderwidth=1, relief="solid")
        self.frm6.pack(expand=True, fill="both")

        test_list = [Rescale]
        
        dropdown = tk.Menubutton(frm5, text="add action", relief="raised")
        dropdown.menu = tk.Menu(dropdown, tearoff=0)
        dropdown["menu"] = dropdown.menu
        for i in test_list:
            dropdown.menu.add_command(label=i.name, command=lambda: self.add_action(i))
        dropdown.pack()
        
        
        
        # self.added_action = tk.StringVar()
        # self.dropdown = ttk.OptionMenu(
        #     frm5,
        #     self.added_action,
        #     test_list[0],
        #     *test_list[1:],
        #     command=self.add_action,
        # )
        # self.dropdown.pack()


        self.bind("<<NotebookTabChanged>>", self.prev_redraw)
        self.bind("<Configure>", self.prev_redraw)

    def __on_root_folder_change(self, *args):
        self.paths = []

        for i in pl.Path(self.root_folder.get()).glob("*.*"):
            self.paths.append(i)
            # print(i)
        self.preview_image_default = Image.open(self.paths[0])
        self.image_prev.config(image=self.preview_image)

    def prev_redraw(self, *args):
        frame_width = self.frm3.winfo_width()
        frame_height = self.frm3.winfo_height()
        self.preview_image_default.size
        factor = min(
            frame_width / self.preview_image_default.size[0],
            frame_height / self.preview_image_default.size[1],
        )
        self.preview_image = scale(self.preview_image_default, factor)
        self.image = ImageTk.PhotoImage(self.preview_image)
        self.image_prev.config(image=self.image)
        print("fac")

    def next_preview(self):
        if self.preview_number + 1 < len(self.paths):
            self.preview_number += 1
            self.preview_image_default = Image.open(self.paths[self.preview_number])
            self.prev_redraw()

    def previos_preview(self):
        if self.preview_number - 1 >= 0:
            self.preview_number -= 1
            self.preview_image_default = Image.open(self.paths[self.preview_number])
            self.prev_redraw()

    def add_action(self, action):
        print("fack", action.name)
        print(self.packed_actions)
        self.packed_actions.append(
            ActionFrame(
                self.frm6,
                action,
                delete_action=self.delete_action,
                move_up=self.move_action_up,
                move_down=self.move_action_down,
            )
        )
        self.packed_actions[-1].pack()

    def update_actions(self):
        for i in self.packed_actions:
            i.forget()
            # print(self.packed_actions)
        for i in self.packed_actions:
            i.pack()
            # print(self.packed_actions)

    def delete_action(self, action: ActionFrame):
        print("delete action working")
        action.destroy()
        self.packed_actions.remove(action)
        # for i in self.packed_actions:
        #     if i.need_delete:
        #         print("debug true")
        #         i.destroy()
        #         self.packed_actions.remove(i)
        #         break

    def move_action_up(self, action: ActionFrame):
        print("moving up")
        if self.packed_actions.index(action) - 1 >= 0:
            print("true shit")
            a, b = (
                self.packed_actions.index(action),
                self.packed_actions.index(action) - 1,
            )
            self.packed_actions[b], self.packed_actions[a] = (
                self.packed_actions[a],
                self.packed_actions[b],
            )
            self.update_actions()

    def move_action_down(self, action: ActionFrame):
        print("moving down")
        if self.packed_actions.index(action) + 1 < len(self.packed_actions):
            print("true shit")
            a, b = (
                self.packed_actions.index(action),
                self.packed_actions.index(action) + 1,
            )
            self.packed_actions[b], self.packed_actions[a] = (
                self.packed_actions[a],
                self.packed_actions[b],
            )
            self.update_actions()

    def apply_actions_preview(self):
        image = self.preview_image
        for i in self.packed_actions:
            image = i.action.forward(image, *i.update_fields_output())
        print(image.size)
        self.preview_image_default = image
        self.prev_redraw()
        