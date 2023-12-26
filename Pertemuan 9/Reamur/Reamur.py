import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def get_fahrenheit():
    suhu = txtsuhu.get()
    F = (9/4 * float(suhu)) + 32
    txtFahrenheit.delete(0,END)
    txtFahrenheit.insert(END,F)

def get_kelvin():
    suhu = txtsuhu.get()
    K = (5/4 * float(suhu)) + 273
    txtKelvin.delete(0,END)
    txtKelvin.insert(END,K)

def get_celcius():
    suhu = txtsuhu.get()
    C = 5/4 * float(suhu) 
    txtCelcius.delete(0,END)
    txtCelcius.insert(END,C)

def hitung():
    get_fahrenheit()
    get_kelvin()
    get_celcius()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Suhu Reamur")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label 
judul = Label(frame, text="Muhammad Daffa Raditha Pratama", fg="darkblue", font=("Arial", 11, "bold"))
judul.grid(row=0, columnspan=2, padx=5, pady=5)
suhu= Label(frame, text="Reamur:")
suhu.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox 
txtsuhu = Entry(frame)
txtsuhu.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

F= Label(frame, text="Fahrenheit:")
F.grid(row=3, column=0, sticky=W, padx=5, pady=5)

K= Label(frame, text="Kelvin:")
K.grid(row=4, column=0, sticky=W, padx=5, pady=5)

C= Label(frame, text="Celcius:")
C.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox 
txtFahrenheit = Entry(frame)
txtFahrenheit.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtKelvin = Entry(frame)
txtKelvin.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtCelcius = Entry(frame)
txtCelcius.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()