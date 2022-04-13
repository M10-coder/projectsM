import tkinter as tk
#
# class Window(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('game')
#
#         label = tk.Label(self,text = 'mi primer program')
#         label.pack(fill=tk.BOTH, expand=1, padx=500,pady=300)
#
# if __name__ == "__main__":
#     window = Window()
#     window.mainloop()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('hello halland')



        self.label = tk.Label(self,text='elije uno')
        self.label.pack(fill=tk.BOTH,expand=1,padx=350,pady=200)

        helloBUtton = tk.Button(self,text = 'say hello',command = self.say_hello)
        helloBUtton.pack(side=tk.LEFT,padx = (20,0),pady=(0,20))

        goodbyeButton = tk.Button(self,text='say adios',command=self.sayAdios)
        goodbyeButton.pack(side=tk.RIGHT,padx=(0,20),pady=(0,20))

    def say_hello(self):
        self.label.configure(text='helloWorld')

    def sayAdios(self):
        self.label.configure(text='adios')
        self.after(2000, self.destroy)

if __name__ == '__main__':
    window = Window()
    window.mainloop()