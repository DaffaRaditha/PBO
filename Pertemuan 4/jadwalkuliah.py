import tkinter as tk
from tkinter import Entry, Button, END, filedialog, Text, LEFT, RIGHT, X, Label

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    pathh.insert(END, tf)
    tf = open(tf)  
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

def savefile():
    file_path = pathh.get()
    with open(file_path, "w") as file1:
        file1.write(txtarea.get(1.0, "end-1c"))

def clearData():
    pathh.delete(0, END)
    txtarea.delete(1.0, "end")
    entry_mata_kuliah.delete(0, END)
    entry_jam.delete(0, END)
    entry_hari.delete(0, END)
    entry_keterangan.delete(0, END)

def saveSchedule():
    mata_kuliah = entry_mata_kuliah.get()
    jam = entry_jam.get()
    hari = entry_hari.get()
    keterangan = entry_keterangan.get()

    schedule_data = f"Mata Kuliah: {mata_kuliah}\nJam: {jam}\nHari: {hari}\nKeterangan: {keterangan}\n\n"
    txtarea.insert(END, schedule_data)

    # Menyimpan data jadwal ke file
    with open(pathh.get(), "a") as file1:
        file1.write(schedule_data)

    # Mengosongkan input setelah disimpan
    entry_mata_kuliah.delete(0, END)
    entry_jam.delete(0, END)
    entry_hari.delete(0, END)
    entry_keterangan.delete(0, END)

ws = tk.Tk()
ws.title("Aplikasi Jadwal Kuliah")
ws.geometry("700x500")  
ws['bg'] = 'green'

txtarea = Text(ws, width=40, height=10)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

Label(ws, text="Mata Kuliah:").pack()
entry_mata_kuliah = Entry(ws)
entry_mata_kuliah.pack(pady=5)

Label(ws, text="Jam:").pack()
entry_jam = Entry(ws)
entry_jam.pack(pady=5)

Label(ws, text="Hari:").pack()
entry_hari = Entry(ws)
entry_hari.pack(pady=5)

Label(ws, text="Keterangan:").pack()
entry_keterangan = Entry(ws)
entry_keterangan.pack(pady=5)

Button(ws, text="Buka File", command=openFile).pack(side=RIGHT, expand=True, fill=X, padx=20)
Button(ws, text="Simpan Jadwal", command=savefile).pack(side=RIGHT, expand=True, fill=X, padx=20)
Button(ws, text="Bersihkan Data", command=clearData).pack(side=RIGHT, expand=True, fill=X, padx=20)
Button(ws, text="Simpan Jadwal Kuliah", command=saveSchedule).pack(side=RIGHT, expand=True, fill=X, padx=20)

ws.mainloop()
