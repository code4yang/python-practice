from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text = 'hello')
        self.helloLabel.pack()

app = App()
app.master.title('hello')
app.mainloop()