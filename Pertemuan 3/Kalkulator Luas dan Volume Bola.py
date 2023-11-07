import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    jari_jari = float(txtjari_jari.get())
    
    L = 4 * 3.14 * jari_jari**2

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    jari_jari = float(txtjari_jari.get())
    
    V =  (4/3) * 3.14 * jari_jari**3
    
    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Bola")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="Muhammad Daffa Raditha Pratama", fg="blue")
nama.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Label Jari-jari
jari_jari = Label(frame, text="Jari-jari:")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari-jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1)

# Button 
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas 
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(frame, text="Volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas 
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5, )

app.mainloop()