import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def get_fahrenheit():
    suhu = txtsuhu.get()
    F = (9/5 * float(suhu)) + 32
    txtFahrenheit.delete(0,END)
    txtFahrenheit.insert(END,F)

def get_reamur():
    suhu = txtsuhu.get()
    R = (4/5 * float(suhu)) 
    txtReamur.delete(0,END)
    txtReamur.insert(END,R)

def get_kelvin():
    suhu = txtsuhu.get()
    K = float(suhu) + 273
    txtKelvin.delete(0,END)
    txtKelvin.insert(END,K)

def hitung():
    get_fahrenheit()
    get_reamur()
    get_kelvin()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Suhu Celcius")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label 
suhu= Label(frame, text="Celcius:")
suhu.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox 
txtsuhu = Entry(frame)
txtsuhu.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

F= Label(frame, text="Fahrenheit:")
F.grid(row=3, column=0, sticky=W, padx=5, pady=5)

R= Label(frame, text="Reamur:")
R.grid(row=4, column=0, sticky=W, padx=5, pady=5)

K= Label(frame, text="Kelvin:")
K.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox 
txtFahrenheit = Entry(frame)
txtFahrenheit.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtReamur = Entry(frame)
txtReamur.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtKelvin = Entry(frame)
txtKelvin.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()