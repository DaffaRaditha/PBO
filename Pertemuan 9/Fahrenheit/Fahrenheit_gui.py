# File-1 (Fahrenheit.py)
class Fahrenheit:
  def __init__(self, suhu):
    self.suhu = suhu

  def get_fahrenheit(self):
    val = self.suhu
    return val
    
  def get_reamur(self):
    val = 4/9 * (self.suhu - 32)
    return val
  
  def get_kelvin(self):
    val = (5/9 * (self.suhu - 32)) + 273
    return val
  
  def get_celcius(self):
    val = 5/9 * (self.suhu - 32)
    return val

# File-2 (FrmFahrenheit.py)
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from Fahrenheit import *
class FrmFahrenheit:
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
        Label(mainFrame, text='Fahrenheit:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=1, column=1, padx=5, pady=5)  

        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5) 

        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5) 

        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=5, column=1, padx=5, pady=5) 

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
    def onHitung(self):
        F = Fahrenheit(int(self.txtFahrenheit.get()))

        # Suhu dalam Reamur
        R = F.get_reamur()
        self.txtReamur.delete(0,END)
        self.txtReamur.insert(END,str(R))

        # Suhu dalam Kelvin
        k = F.get_kelvin()
        self.txtKelvin.delete(0,END)
        self.txtKelvin.insert(END,str(K))

        # Suhu dalam Celcius
        C = F.get_celcius()
        self.txtCelcius.delete(0,END)
        self.txtCelcius.insert(END,str(C))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmFahrenheit(root, "Program Konversi Suhu Fahrenheit")
    root.mainloop() 