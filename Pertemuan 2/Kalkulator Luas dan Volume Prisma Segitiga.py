import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas_selimut():
    alas = float(txtalas.get())
    tinggi_prisma = float(txttinggi_prisma.get())

    LS = (alas + alas + alas) * tinggi_prisma

    txtLuas_Selimut.delete(0,END)
    txtLuas_Selimut.insert(END,LS)

def hitung_luas_permukaan():
    alas = float(txtalas.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())
    tinggi_prisma = float(txttinggi_prisma.get())

    LP = ((alas + alas + alas) * tinggi_prisma) + alas * tinggi_segitiga

    txtLuas_Permukaan.delete(0,END)
    txtLuas_Permukaan.insert(END,LP)

def hitung_volume():
    alas = float(txtalas.get())
    tinggi_segitiga = float(txttinggi_segitiga.get())
    tinggi_prisma = float(txttinggi_prisma.get())
    
    V =  0.5 * alas * tinggi_segitiga * tinggi_prisma
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Prisma Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Muhammad Daffa Raditha Pratama", fg="blue")
nama.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Label Alas
alas = Label(frame, text="Alas:")
alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Segitiga
tinggi_segitiga = Label(frame, text="Tinggi Segitiga:")
tinggi_segitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Prisma
tinggi_prisma = Label(frame, text="Tinggi Prisma:")
tinggi_prisma.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Alas
txtalas = Entry(frame)
txtalas.grid(row=1, column=1)

# Textbox Tinggi Segitiga
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=2, column=1)

# Textbox Tinggi Prisma
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=3, column=1)

# Button 
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut: ")
luas_selimut.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan: ")
luas_permukaan.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(frame, text="Volume: ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtLuas_Selimut = Entry(frame)
txtLuas_Selimut.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Segitiga
txtLuas_Permukaan = Entry(frame)
txtLuas_Permukaan.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=7, column=1, sticky=W, padx=5, pady=5, )

app.mainloop()