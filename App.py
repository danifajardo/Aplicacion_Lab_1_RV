from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image

class App(Tk):
    def __init__(self, widht, height, projectName):
        Tk.__init__(self)
        self.widht = int(widht)
        self.height = int(height)
        self.firstImg = None
        self.secondImg = None
        Tk.geometry(self, widht+"x"+height)
        Tk.title(self, projectName)
        #Tk.resizable(self, False, False)
        self.framset()

    def framset(self):
        #Main Menu Bar
        newMenu = Menu(self)
        self.config(menu=newMenu)

        #First Panel
        frame = Frame(self, bg= '#000000')
        frame.config(width=self.widht/2, height=self.height/2)
        frame.pack(side=LEFT, expand=True, fill=BOTH)

        #Second Panel
        frame2 = Frame(self, bg= '#0000CC')
        frame2.config(width=self.widht/2, height=self.height/2)
        frame2.pack(side=RIGHT, expand=True, fill=BOTH)

        #File Menu
        fileMenu = Menu(newMenu, tearoff="off")
        newMenu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Add First Image", command=lambda: self.uploadImage(panel = frame, anchor = 1))
        fileMenu.add_command(label="Add Second Image", command=lambda: self.uploadImage(panel = frame2, anchor = 2))

        #Run Menu
        runMenu = Menu(newMenu, tearoff="off")
        newMenu.add_cascade(label="Run", menu=runMenu)
        runMenu.add_cascade(label="First Method", command=lambda: self.runMethod(method = 1))
        runMenu.add_cascade(label="Second Method", command=lambda: self.runMethod(method = 2))
        runMenu.add_cascade(label="Third Method", command=lambda: self.runMethod(method = 3))
        
        
    def uploadImage(self, panel, anchor):
        path = filedialog.askopenfile()
        imagePath = Image.open(path.name)
        newSize = (int(self.widht/2),int(self.height))
        imageResized = imagePath.resize(newSize, Image.ANTIALIAS)
        if anchor == 1 and self.firstImg == None:
            self.firstImg = ImageTk.PhotoImage(imageResized)
            label = Label(panel, image = self.firstImg)
            label.configure(image=self.firstImg)
        else :
            self.secondImg = ImageTk.PhotoImage(imageResized)
            label = Label(panel, image = self.secondImg) 
        label.pack()
        print(panel.nametowidget)

    def runMethod(self, method):
        print("Ok")
