from Tkinter import *

class Window(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("GUI")
        self.master.configure(background="white")
        self.grid()

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label="Exit", command=self.exit)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)

        edit.add_command(label="fr AR to SW", command=self.A2S)
        edit.add_command(label="fr SW to AR", command="self.S2A")

        menu.add_cascade(label="option", menu=edit)

        Label(self.master, text="enter word:", bg="white", fg="black", font= "none 12 bold") .grid(row=6, column=0, sticky=W)

        self.textentry= Entry(self.master, width=20, bg="white")
        self.textentry.grid(row=7, column=0, sticky=W)

        Button(self.master, text="Translate", width=6, command=self.BsmALLAH) .grid(row=8, column=0, sticky=W)

        Label(self.master, text="Meaning:", bg="white", fg="black", font= "none 12 bold") .grid(row=9, column=0, sticky=W)

        self.result= Text(self.master, width=75, height=6, background="white")
        self.result.grid(row=10, column=0, columnspan=1, sticky=W)


    def A2S(self):
        self.ArDict= {
            'ar':'a',
            'ar':'b, B',
            'ar': 't, T'
        }
        print("BMLLH")

    def S2A(self):
        print("LHMLH")
        SwDict= {
            'e': "AR",
            'f': "AR",
            's': "AR",
        }
        print("LHMDL")

    def BsmALLAH(self):
        print("LHKBR")

        textentry= self.textentry.get()
        self.result.delete(0.0, END)
        try:
            Meaning= ArDict[textentry]
        except:
            Meaning= "not found"
        self.result.insert(END, Meaning)

    def exit(self):
        exit()


# would be the only window
root = Tk()

root.geometry("400x300")

app = Window(root)


#mainloop
root.mainloop()