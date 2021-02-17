from tkinter import *
from functools import partial

root = Tk()
button_identities = []
Label_identities = []
lines = []


def add_one_stuff_to_the_file(new_info):
    file_which_u_are_sing = open("smghere.txt", "a")
    file_which_u_are_sing.write(new_info)
    file_which_u_are_sing.write("\n")
    file_which_u_are_sing.close()


def counter_for_the_lines():

    with open("smghere.txt") as file_in:

        for line in file_in:
            lines.append(line)


def file_command():

    file = open("smghere.txt", "r+")
    file.truncate(0)
    file.close()
    file_which_u_are_sing = open("smghere.txt", "a")

    for item in lines:
        file_which_u_are_sing.write(item)
    file_which_u_are_sing.close()


def clear():
    clear_list = root.grid_slaves()
    for clear_item in clear_list:
        clear_item.destroy()


def change(n):

    print(n-1)
    lines.pop(n-1)
    print(lines)
    button_identities.clear()
    Label_identities.clear()
    clear()
    file_command()
    print(lines)
    entry_button_starter()
    button_generation()


def button_generation():

    x = 1
    for smg in lines:

        xy = Label(root, text=smg)
        xy.grid(row=x, column=0)
        b1 = Button(root, text="Delete", command=partial(change, x))
        b1.grid(row=x, column=2)
        Label_identities.append(xy)
        button_identities.append(b1)
        x = x + 1


def entry_button_starter():
    def entry_button_command(en):
        new_info = entry.get()
        print(new_info)
        lines.append(new_info + "\n")
        add_one_stuff_to_the_file(new_info)
        button_identities.clear()
        Label_identities.clear()
        clear()
        entry_button_starter()
        button_generation()

    entry = Entry(root, )
    entry.grid(row=0, column=0)

    ok_button = Button(root, text="OK", command=lambda: entry_button_command)
    ok_button.grid(row=0, column=1)
    entry.bind('<Return>', entry_button_command)


counter_for_the_lines()
entry_button_starter()
button_generation()

root.mainloop()
