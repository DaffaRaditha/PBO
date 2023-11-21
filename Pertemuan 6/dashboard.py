import tkinter as tk
from tkinter import Menu
from Balok import *
from Bola import *
from Kerucut import *
from Kubus import *
from LimasSegiempat import *
from LimasSegitiga import *
from PersegiPanjang import *
from PrismaSegitiga import *
from Silinder import *

# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Balok', command= lambda: new_window("Balok", Balok)
)
app_menu.add_command(
    label='App Bola', command= lambda: new_window("Bola", Bola)
)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Kerucut", Kerucut)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Kubus", Kubus)
)
app_menu.add_command(
    label='App Limas Segiempat', command= lambda: new_window("Limas Segiempat", LimasSegiempat)
)
app_menu.add_command(
    label='App Limas Segitiga', command= lambda: new_window("Limas Segitiga", LimasSegitiga)
)
app_menu.add_command(
    label='App Persegi Panjang', command= lambda: new_window("Persegi Panjang", PersegiPanjang)
)
app_menu.add_command(
    label='App Prisma Segitiga', command= lambda: new_window("Prisma Segitiga", PrismaSegitiga)
)
app_menu.add_command(
    label='App Silinder', command= lambda: new_window("Silinder", Silinder)
)


def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
    
root.mainloop()