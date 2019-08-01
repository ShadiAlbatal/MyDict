# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals
from Tkinter import *
from langdetect import detect
import Swedish2Arabic
import Arabic2Swedish

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
        menu.add_cascade(label="File", menu=file)
        file.add_command(label="Exit", command=self.exit)


        edit = Menu(menu)
        menu.add_cascade(label="Help", menu=edit)
        edit.add_command(label="About", command="")

        Label(self.master, text="enter word:", bg="white", fg="black", font= "none 12 bold") .grid(row=6, column=0, sticky=W)

        self.textentry= Entry(self.master, width=20, bg="white")
        self.textentry.grid(row=7, column=0, sticky=W)

        Button(self.master, text="Translate", width=6, command=self.BsmALLAH) .grid(row=8, column=0, sticky=W)

        Label(self.master, text="Meaning:", bg="white", fg="black", font= "none 12 bold") .grid(row=9, column=0, sticky=W)

        self.result= Text(self.master, width=75, height=6, background="white")
        self.result.grid(row=10, column=0, columnspan=1, sticky=W)

    def BsmALLAH(self):
            print("LHKBR")
            textentry= self.textentry.get()
            self.result.delete(0.0, END)
            v= detect(textentry)
            d= v.encode('ascii','ignore')
            if d=='ar':
                try:
                    Meaning= Arabic2Swedish.ArDict[textentry]
                except:
                    Meaning= "not found"
                self.result.insert(END, Meaning)
            elif d=='sv':
                try:
                    Meaning= Swedish2Arabic.SwDict[textentry]
                except:
                    Meaning= "not found"
                self.result.insert(END, Meaning)
            else:
                Meaning= "try something else"
                self.result.insert(END, Meaning)


    def exit(self):
        exit()


# would be the only window
root = Tk()

root.geometry("400x300")

app = Window(root)


#mainloop
root.mainloop()