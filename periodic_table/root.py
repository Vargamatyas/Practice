import tkinter as tk

LARGE_FONT = ("verdana", 12)


class Root(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = [StartPage]

        frame = StartPage(container, self)

        self.frames[0] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(0)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        


app = Root()
app.mainloop()
