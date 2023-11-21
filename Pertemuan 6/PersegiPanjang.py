from tkinter import Frame, Label, Entry, Button, END, Tk

class PersegiPanjang:
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
        Label(mainFrame, text='Panjang:').grid(row=1, column=0, padx=5, pady=5)
        Label(mainFrame, text='Lebar:').grid(row=2, column=0, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=4, column=0, padx=5, pady=5)
        Label(mainFrame, text='Keliling:').grid(row=5, column=0, padx=5, pady=5)

        # Textbox
        self.txtPanjang = Entry(mainFrame)
        self.txtPanjang.grid(row=1, column=1, padx=5, pady=5)
        self.txtLebar = Entry(mainFrame)
        self.txtLebar.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=5, column=1, padx=5, pady=5)

        # Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=3, columnspan=2, padx=5, pady=5)
        
    def onHitung(self):
        panjang = float(self.txtPanjang.get())
        lebar = float(self.txtLebar.get())
        
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        
        self.txtLuas.delete(0, END)
        self.txtKeliling.delete(0, END)
        self.txtLuas.insert(END, str(luas))
        self.txtKeliling.insert(END, str(keliling))
               
    def onKeluar(self):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = PersegiPanjang(root, "Program Luas dan Keliling Persegi Panjang")
    root.mainloop()
