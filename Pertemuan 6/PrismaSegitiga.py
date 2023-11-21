from tkinter import Frame, Label, Entry, Button, END, Tk

class PrismaSegitiga:
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
        Label(mainFrame, text='Luas Alas:').grid(row=1, column=0, padx=5, pady=5)
        Label(mainFrame, text='Tinggi Prisma:').grid(row=2, column=0, padx=5, pady=5)
        Label(mainFrame, text='Luas:').grid(row=4, column=0, padx=5, pady=5)
        Label(mainFrame, text='Volume:').grid(row=5, column=0, padx=5, pady=5)

        # Textbox
        self.txtLuasAlas = Entry(mainFrame)
        self.txtLuasAlas.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiPrisma = Entry(mainFrame)
        self.txtTinggiPrisma.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=5, column=1, padx=5, pady=5)

        # Button
        self.btnHitung = Button(mainFrame, text='Hitung', command=self.onHitung)
        self.btnHitung.grid(row=3, columnspan=2, padx=5, pady=5)
        
    def onHitung(self):
        luas_alas = float(self.txtLuasAlas.get())
        tinggi_prisma = float(self.txtTinggiPrisma.get())
        
        luas_permukaan = luas_alas + (3 * (luas_alas ** 0.5) * tinggi_prisma)
        volume = (1/2) * luas_alas * tinggi_prisma
        
        self.txtLuas.delete(0, END)
        self.txtVolume.delete(0, END)
        self.txtLuas.insert(END, str(luas_permukaan))
        self.txtVolume.insert(END, str(volume))
               
    def onKeluar(self):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = PrismaSegitiga(root, "Program Luas dan Volume Prisma Segitiga")
    root.mainloop()
