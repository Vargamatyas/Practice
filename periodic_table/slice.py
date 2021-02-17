from tkinter import *

root = Tk()


class Labeel:

    def __init__(self, name, row, column, bg):

        self.name = name
        self.row = row
        self.column = column
        self.bg = bg
        yx = Label(root, text=self.name, font=("H", 10), width=7, height=4, bg=self.bg)
        yx.grid(row=self.row, column=self.column)


Labeel0 = Labeel("", 0, 0, '#FFFFFF')
Labeel1 = Labeel("1.", 0, 1, '#FFFFFF')
Labeel2 = Labeel("2.", 0, 2, '#FFFFFF')
Labeel3 = Labeel("3.", 0, 3, '#FFFFFF')
Labeel4 = Labeel("4.", 0, 4, '#FFFFFF')
Labeel5 = Labeel("5.", 0, 5, '#FFFFFF')
Labeel6 = Labeel("6.", 0, 6, '#FFFFFF')
Labeel7 = Labeel("7.", 0, 7, '#FFFFFF')
Labeel8 = Labeel("8.", 0, 8, '#FFFFFF')
Labeel9 = Labeel("9.", 0, 9, '#FFFFFF')
Labeel10 = Labeel("10.", 0, 10, '#FFFFFF')
Labeel11 = Labeel("11.", 0, 11, '#FFFFFF')
Labeel12 = Labeel("12.", 0, 12, '#FFFFFF')
Labeel13 = Labeel("13.", 0, 13, '#FFFFFF')
Labeel14 = Labeel("14.", 0, 14, '#FFFFFF')
Labeel15 = Labeel("15.", 0, 15, '#FFFFFF')
Labeel16 = Labeel("16.", 0, 16, '#FFFFFF')
Labeel17 = Labeel("17.", 0, 17, '#FFFFFF')
Labeel18 = Labeel("18.", 0, 18, '#FFFFFF')
Labeel19 = Labeel("1.", 1, 0, '#FFFFFF')
Labeel20 = Labeel("2.", 2, 0, '#FFFFFF')
Labeel21 = Labeel("3.", 3, 0, '#FFFFFF')
Labeel22 = Labeel("4.", 4, 0, '#FFFFFF')
Labeel23 = Labeel("5.", 5, 0, '#FFFFFF')
Labeel24 = Labeel("6.", 6, 0, '#FFFFFF')
Labeel25 = Labeel("7.", 7, 0, '#FFFFFF')


class Atom:

    def __init__(self, name, row, column, mass, bg, click_colour, valid):

        self.name = name
        self.row = row
        self.column = column
        self.mass = str(mass)
        self.bg = bg
        self.click_colour = click_colour
        self.valid = valid
        if self.valid == "enable":
            xy = Button(root, text=self.name, font=("H", 10), width=7, height=4,
                        command=lambda: Atom.command1(self), bg=self.bg)
            xy.grid(row=self.row, column=self.column)
        else:
           pass

    def command1(self):
        xyz = Button(root, text=self.mass, font=(self.mass, 10), width=7, height=4,
                     command=lambda: Atom.newlabel(self), bg=self.click_colour)
        xyz.grid(row=self.row, column=self.column)

    def newlabel(self):
        newlabel = Button(root, text=self.name, font=(self.name, 10), width=7, height=4,
                          command=lambda: Atom.command1(self), bg=self.bg)
        newlabel.grid(row=self.row, column=self.column)


sarga = "#FFFF98"
sarga2 = "#FFFF75"
h = Atom("H", 1, 1, 1.0079, sarga, sarga2, "enable")
li = Atom("Li", 2, 1, 6.941, "#F56767", "#CC5656", "enable")
ba = Atom("Ba", 6, 2, 137.327, "#FFDA99", "#D9B882", "enable")
ag = Atom("Ag", 5, 11, 107.8682, "#FF97A5", "#D9808C", "enable")
la = Atom("La", 6, 3, 138.9055, "#DAB8F5", "#CAAAE3", "enable")
u = Atom("U", 10, 6, 237, "#E29CFF", "#BF84D9", "enable")
o = Atom("O", 2, 16, 15.9994, "#FFFF98", "#FFFF75", "enable")
si = Atom("Si", 3, 14, 28.0855, "#92BDA0", "#84AB91", "enable")


root.mainloop()
