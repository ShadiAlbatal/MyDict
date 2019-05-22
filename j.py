from tkinter import *
from PIL import Image, ImageTk

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

        edit.add_command(label="fr AR to SW", command=self.AD)
        edit.add_command(label="fr SW to AR", command=self.SD)

        menu.add_cascade(label="option", menu=edit)  
       
        load = Image.open('D:\myPy\dicto\logo.gif')
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self.master, image=render)
        img.image = render
        img.grid(row=0, column=0, sticky=W)

        Label(self.master, text="enter word:", bg="white", fg="black", font= "none 12 bold") .grid(row=6, column=0, sticky=W)

        textentry= Entry(self.master, width=20, bg="white") .grid(row=7, column=0, sticky=W)

        Button(self.master, text="Translate", width=6, command="") .grid(row=8, column=0, sticky=W)

        Label (self.master, text="Meaning:", bg="white", fg="black", font= "none 12 bold") .grid(row=9, column=0, sticky=W)   
        
        result= Text(self.master, width=75, height=6, background="white") .grid(row=10, column=0, columnspan=1, sticky=W)
        
    def AD(self):
        ArDict= {
            'أ':'a',
            'ب':'b, B',
            'ت': 't, T',
        }
        return True
        
    def SD(self):
        SwDict= {
            'e': "ياء",
            'f': "فاء",
            's': "سين",
        }
        return True
        
    def StA():
        textentry= textentry.get()
        result.delete(0.0, END)
        try:
            Meaning= SwDict[textentry]
        except:
            Meaning= "finns inte"
        result.insert(END, Meaning)
        
    def A2S():
        textentry= textentry.get()
        result.delete(0.0, END)
        try:
            Meaning= ArDict[textentry]
        except:
            Meaning= "رب لك الحمد"
        result.insert(END, Meaning)
            
    def submit():
        if AD is True:
            S2A()
        else:
            A2S()

    def A2S(self):
        print("BMLLH")
        return True

    def S2A(self):
        print("LHMLH")
        return True

    def exit(self):
        exit()


# would be the only window
root = Tk()

root.geometry("400x300")

app = Window(root)


#mainloop 
root.mainloop()  