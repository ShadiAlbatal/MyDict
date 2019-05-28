from Tkinter import *

class Window(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label="Exit", command=self.exit)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)

        edit.add_command(label="fr AR to SW", command=self.A2S)
        edit.add_command(label="fr SW to AR", command=self.S2A)

        menu.add_cascade(label="option", menu=edit)

        self.master.title("GUI")
        self.master.configure(background="white")
        self.grid()

        Label(self.master, text="enter word:", bg="white", fg="black", font= "none 12 bold") .grid(row=6, column=0, sticky=W)

        self.textentry= Entry(self.master, width=20, bg="white")
        self.textentry.grid(row=7, column=0, sticky=W)

        Button(self.master, text="Translate", width=6, command= self.BsmALLAH) .grid(row=8, column=0, sticky=W)

        Label(self.master, text="Meaning:", bg="white", fg="black", font= "none 12 bold") .grid(row=9, column=0, sticky=W)

        self.result= Text(self.master, width=75, height=6, background="white")
        self.result.grid(row=10, column=0, columnspan=1, sticky=W)

    def A2S(self):
        print("LKLHMD")
    #    return True
        return self.A2S is True
        return self.S2A is False


    def S2A(self):
        print("RBSBHNK")
    #    return True
        return self.S2A is True
        return self.A2S is False

    def BsmALLAH(self):
        if self.A2S:
            print("LHKBR")
            ArDict= {
                'ar':'a',
                'ar':'b, B',
                'ar': 't, T'
            }
            textentry= self.textentry.get()
            self.result.delete(0.0, END)
            try:
                Meaning= ArDict[textentry]
            except:
                Meaning= "not found"
            self.result.insert(END, Meaning)

        elif self.S2A:
            print("LILILLH")
            SwDict= {
            'e': "AR",
            'f': "vR",
            's': "sR",
            }
            textentry= self.textentry.get()
            self.result.delete(0.0, END)
            try:
                Meaning= SwDict[textentry]
            except:
                Meaning= "not found"
            self.result.insert(END, Meaning)
        else:
            Meaning= "please select a langauge from option menu"
            self.result.insert(END, Meaning)


    def exit(self):
        exit()

# would be the only window
root = Tk()

root.geometry("400x300")

app = Window(root)


#mainloop
root.mainloop()