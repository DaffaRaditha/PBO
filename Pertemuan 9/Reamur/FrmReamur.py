from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmReamur:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES) 
        Label(mainFrame, text='Muhammad Daffa Raditha Pratama', fg="black", font=("Arial", 11, "bold")).grid(row=0, columnspan=2,
            padx=5, pady=5)
        Label(mainFrame, text='Reamur:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="kelvin:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=1, column=1, padx=5, pady=5)  

        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=3, column=1, padx=5, pady=5) 

        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5) 

        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=5, column=1, padx=5, pady=5) 
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)

    def get_fahrenheit(self, suhu):
        val = (9/4 * suhu) + 32
        return val
    
    def get_kelvin(self, suhu):
        val = (5/4 * suhu) + 273
        return val
    
    def get_celcius(self, suhu):
        val = 5/4 * suhu 
        return val

    def onHitung(self):
        # Suhu dalam Fahrenheit
        suhu = self.txtReamur.get()
        F = self.get_fahrenheit(float(suhu))
        self.txtFahrenheit.delete(0,END)
        self.txtFahrenheit.insert(END,str(F))

        # Suhu dalam Kelvin
        K = self.get_kelvin(float(suhu))
        self.txtKelvin.delete(0,END)
        self.txtKelvin.insert(END,str(K))

        # Suhu dalam Celcius
        C = self.get_celcius(float(suhu))
        self.txtCelcius.delete(0,END)
        self.txtCelcius.insert(END,str(C))
        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()            


if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmReamur(root, "Program Konversi Suhu Reamur")
    root.mainloop() 