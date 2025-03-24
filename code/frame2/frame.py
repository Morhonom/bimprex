from tkinter import ttk


class Frame2(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.preset()

    def preset(self):
        frm1 = ttk.Frame(self, borderwidth=2, relief="solid")
        frm1.pack(side="left", fill="both", expand=True)
        frm2 = ttk.Frame(self, borderwidth=2, relief="solid")
        frm2.pack(side="left", fill="both", expand=True)
        
        frm3 = ttk.Frame(frm2, borderwidth=2, relief="solid")
        frm3.pack(anchor="n", expand=True, fill="both")
        
        button_previus = ttk.Button(frm2, text="left")
        # button_next = ttk.Button(frm2, text="right")
        # button_change = ttk.Button(frm2, text="change")
        button_previus.pack()
        # button_next.pack(anchor="sw", side="left")
        # button_change.pack(anchor="sw", side="left")
        