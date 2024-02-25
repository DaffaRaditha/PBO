# filename : FrmProperti.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Properti import Properti
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
class FormProperti:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1000x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='KODE_TEMPAT:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox KODE_TEMPAT
        self.txtKODE_TEMPAT = Entry(mainFrame) 
        self.txtKODE_TEMPAT.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKODE_TEMPAT.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='NOMOR_KTP:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOMOR_KTP
        self.txtNOMOR_KTP = Entry(mainFrame) 
        self.txtNOMOR_KTP.grid(row=1, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='NOMOR_HP:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOMOR_HP
        self.txtNOMOR_HP = Entry(mainFrame) 
        self.txtNOMOR_HP.grid(row=2, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='NAMA_PELANGGAN:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_PELANGGAN
        self.txtNAMA_PELANGGAN = Entry(mainFrame) 
        self.txtNAMA_PELANGGAN.grid(row=3, column=1, padx=5, pady=5)
                
         # date 
        Label(mainFrame, text='TANGGAL:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=4, column=1, padx=5, pady=5)
                    
         # date 
        Label(mainFrame, text='TANGGAL_MULAI:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL_MULAI
        self.txtTANGGAL_MULAI = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL_MULAI.grid(row=5, column=1, padx=5, pady=5)
                    
         # date 
        Label(mainFrame, text='TANGGAL_SELESAI:').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL_SELESAI
        self.txtTANGGAL_SELESAI = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL_SELESAI.grid(row=6, column=1, padx=5, pady=5)
                    
         # int 
        Label(mainFrame, text='TARIF:').grid(row=0, column=2, sticky=W, padx=5, pady=5)
        # Textbox TARIF
        self.txtTARIF = Entry(mainFrame) 
        self.txtTARIF.grid(row=0, column=3, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='TOTAL_BAYAR:').grid(row=1, column=2, sticky=W, padx=5, pady=5)
        # Textbox TOTAL_BAYAR
        self.txtTOTAL_BAYAR = Entry(mainFrame) 
        self.txtTOTAL_BAYAR.grid(row=1, column=3, padx=5, pady=5)
                
         # enum 
        Label(mainFrame, text='STATUS_BAYAR:').grid(row=2, column=2, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtSTATUS_BAYAR = StringVar()
        CboSTATUS_BAYAR = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtSTATUS_BAYAR) 
        CboSTATUS_BAYAR.grid(row=2, column=3, padx=5, pady=5)
        # Adding combobox drop down list
        CboSTATUS_BAYAR['values'] = ('tagihan','lunas')
        CboSTATUS_BAYAR.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=3, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=4, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=5, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','kode_tempat','nomor_ktp','nomor_hp','nama_pelanggan','tanggal','tanggal_mulai','tanggal_selesai','tarif','total_bayar','status_bayar')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('kode_tempat', text='kode_tempat')
        self.tree.column('kode_tempat', width="30")
        self.tree.heading('nomor_ktp', text='nomor_ktp')
        self.tree.column('nomor_ktp', width="100")
        self.tree.heading('nomor_hp', text='nomor_hp')
        self.tree.column('nomor_hp', width="100")
        self.tree.heading('nama_pelanggan', text='nama_pelanggan')
        self.tree.column('nama_pelanggan', width="100")
        self.tree.heading('tanggal', text='tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('tanggal_mulai', text='tanggal_mulai')
        self.tree.column('tanggal_mulai', width="100")
        self.tree.heading('tanggal_selesai', text='tanggal_selesai')
        self.tree.column('tanggal_selesai', width="100")
        self.tree.heading('tarif', text='tarif')
        self.tree.column('tarif', width="100")
        self.tree.heading('total_bayar', text='total_bayar')
        self.tree.column('total_bayar', width="100")
        self.tree.heading('status_bayar', text='status_bayar')
        self.tree.column('status_bayar', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtKODE_TEMPAT.delete(0,END)
        self.txtKODE_TEMPAT.insert(END,"")
                                
        self.txtNOMOR_KTP.delete(0,END)
        self.txtNOMOR_KTP.insert(END,"")
                                
        self.txtNOMOR_HP.delete(0,END)
        self.txtNOMOR_HP.insert(END,"")
                                
        self.txtNAMA_PELANGGAN.delete(0,END)
        self.txtNAMA_PELANGGAN.insert(END,"")
                                
        self.txtTARIF.delete(0,END)
        self.txtTARIF.insert(END,"")
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,"")
                                
        self.txtSTATUS_BAYAR.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data properti
        obj = Properti()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        kode_tempat = self.txtKODE_TEMPAT.get()
        obj = Properti()
        res = obj.getByKODE_TEMPAT(kode_tempat)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        kode_tempat = self.txtKODE_TEMPAT.get()
        obj = Properti()
        res = obj.getByKODE_TEMPAT(kode_tempat)
            
        self.txtNOMOR_KTP.delete(0,END)
        self.txtNOMOR_KTP.insert(END,obj.nomor_ktp)
                                
        self.txtNOMOR_HP.delete(0,END)
        self.txtNOMOR_HP.insert(END,obj.nomor_hp)
                                
        self.txtNAMA_PELANGGAN.delete(0,END)
        self.txtNAMA_PELANGGAN.insert(END,obj.nama_pelanggan)
                                
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)
                                
        self.txtTANGGAL_MULAI.delete(0,END)
        self.txtTANGGAL_MULAI.insert(END,obj.tanggal_mulai)
                                
        self.txtTANGGAL_SELESAI.delete(0,END)
        self.txtTANGGAL_SELESAI.insert(END,obj.tanggal_selesai)
                                
        self.txtTARIF.delete(0,END)
        self.txtTARIF.insert(END,obj.tarif)
                                
        self.txtTOTAL_BAYAR.delete(0,END)
        self.txtTOTAL_BAYAR.insert(END,obj.total_bayar)
                                
        self.txtSTATUS_BAYAR.set(obj.status_bayar)
            
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        kode_tempat = self.txtKODE_TEMPAT.get()
        nomor_ktp = self.txtNOMOR_KTP.get()
        nomor_hp = self.txtNOMOR_HP.get()
        nama_pelanggan = self.txtNAMA_PELANGGAN.get()
        tanggal = self.txtTANGGAL.get()
        tanggal_mulai = self.txtTANGGAL_MULAI.get()
        tanggal_selesai = self.txtTANGGAL_SELESAI.get()
        tarif = self.txtTARIF.get()
        total_bayar = self.txtTOTAL_BAYAR.get()
        status_bayar = self.txtSTATUS_BAYAR.get()       
        obj = Properti()
        obj.kode_tempat = kode_tempat
        obj.nomor_ktp = nomor_ktp
        obj.nomor_hp = nomor_hp
        obj.nama_pelanggan = nama_pelanggan
        obj.tanggal = tanggal
        obj.tanggal_mulai = tanggal_mulai
        obj.tanggal_selesai = tanggal_selesai
        obj.tarif = tarif
        obj.total_bayar = total_bayar
        obj.status_bayar = status_bayar
        if(self.ditemukan==True):
            res = obj.updateByKODE_TEMPAT(kode_tempat)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        kode_tempat = self.txtKODE_TEMPAT.get()
        obj = Properti()
        obj.kode_tempat = kode_tempat
        if(self.ditemukan==True):
            res = obj.deleteByKODE_TEMPAT(kode_tempat)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormProperti(root, "Aplikasi Data Properti")
    root.mainloop() 