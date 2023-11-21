from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text=' Belanda:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='China:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Spanyol:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        # Label judul
        Label(mainFrame, text='Muhammad Daffa Raditha Pratama',
              font=("Arial", 11, "bold")).grid(row=0, columnspan=2, padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=1, column=1, padx=5, pady=5)

        self.txtHasil1 = Entry(mainFrame, width=50) 
        self.txtHasil1.grid(row=3, column=1, padx=5, pady=5)

        self.txtHasil2 = Entry(mainFrame, width=50) 
        self.txtHasil2.grid(row=4, column=1, padx=5, pady=5)

        self.txtHasil3 = Entry(mainFrame, width=50) 
        self.txtHasil3.grid(row=5, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!',
            command=self.onTranslate)
        self.btnTranslate.grid(row=2, column=1, padx=5, pady=5) 

    def onTranslate(self):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        hasil1 = penterjemah.translate(self.txtSumber.get(), src='id', dest='nl') 

        hasil2 = penterjemah.translate(self.txtSumber.get(), src='id', dest='zh-cn') 

        hasil3 = penterjemah.translate(self.txtSumber.get(), src='id', dest='es') 
       
        # menampilkan hasil terjemahan
        self.txtHasil1.insert(END,hasil1.text)

        self.txtHasil2.insert(END,hasil2.text)

        self.txtHasil3.insert(END,hasil3.text)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop() 