import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas_selimut():
    jari_jari = float(txtjari_jari.get())
    garis_pelukis = float(txtgaris_pelukis.get())
    
    LS = 3.14 * jari_jari * garis_pelukis

    txtLuas_Selimut.delete(0, END)
    txtLuas_Selimut.insert(END, LS)

def hitung_luas_permukaan():
    jari_jari = float(txtjari_jari.get())
    garis_pelukis = float(txtgaris_pelukis.get())
    
    LP = (3.14 * jari_jari * garis_pelukis) + 3.14 * jari_jari**2

    txtLuas_Permukaan.delete(0, END)
    txtLuas_Permukaan.insert(END, LP)

def hitung_volume():
    jari_jari = float(txtjari_jari.get())
    tinggi = float(txttinggi.get())
    
    V = (1/3) * 3.14 * jari_jari**2 * tinggi
    
    txtVolume.delete(0, END)
    txtVolume.insert(END, V)

def hitung():
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Windows
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kerucut")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Muhammad Daffa Raditha Pratama", fg="blue")
nama.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Label Jari-jari
jari_jari = Label(frame, text="Jari-jari:")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)
                
# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Garis Pelukis
garis_pelukis = Label(frame, text="Garis Pelukis:")
garis_pelukis.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari-jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Textbox Garis Pelukis
txtgaris_pelukis = Entry(frame)
txtgaris_pelukis.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut: ")
luas_selimut.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan: ")
luas_permukaan.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume: ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtLuas_Selimut = Entry(frame)
txtLuas_Selimut.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Permukaan = Entry(frame)
txtLuas_Permukaan.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
