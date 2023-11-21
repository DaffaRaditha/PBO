from tkinter import Frame, Label, Entry, Button, END, Tk
import math

class Bola:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack()

        # Label
        Label(mainFrame, text='Muhammad Daffa Raditha Pratama',
              font=("Arial", 11, "bold")).grid(row=0, columnspan=2, padx=5, pady=5)
        Label(mainFrame, text='Jari-jari:').grid(row=1, column=0, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=3, column=0, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=4, column=0, padx=5, pady=5)

        # Textbox
        self.txtJariJari = Entry(mainFrame)
        self.txtJariJari.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=4, column=1, padx=5, pady=5)

        # Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=2, columnspan=2, padx=5, pady=5)
        
    def onHitung(self):
        jari_jari = float(self.txtJariJari.get())
        
        luas_permukaan = 4 * math.pi * (jari_jari ** 2)
        volume = (4/3) * math.pi * (jari_jari ** 3)
        
        self.txtLuas.delete(0, END)
        self.txtVolume.delete(0, END)
        self.txtLuas.insert(END, str(luas_permukaan))
        self.txtVolume.insert(END, str(volume))
               
    def onKeluar(self):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = Bola(root, "Program Luas dan Volume Bola")
    root.mainloop()
