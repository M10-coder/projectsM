import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('primera parte')
        var = tk()
        var.setvar(name='str',value='eleji')

        self.label = tk.Label(self,text=strv)
        self.label.pack(fill=tk.BOTH,expand=1,padx=100,pady=30)

        helloB = tk.Button(self,text='saludar',command=self.saludar)
        helloB.pack(side=tk.LEFT,padx=(20,0),pady=(0,20))

        salirB= tk.Button(self,text='X',command=self.salir)
        salirB.pack(side=tk.RIGHT,padx=(0,20),pady=(20,0))

    def saludar(self):
        self.var = tk.StringVar()
        self.var.set("hola")
        self.var.get()

    def salir(self):
        self.var.set("adios")
        self.after(2000,self.destroy)

if __name__ == '__main__':
    window = Window()
    window.mainloop()