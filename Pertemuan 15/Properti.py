# filename : Properti.py
from db import DBConnection as mydb
class Properti:
    def __init__(self):
        self.__id=None
        self.__kode_tempat=None
        self.__nomor_ktp=None
        self.__nomor_hp=None
        self.__nama_pelanggan=None
        self.__tanggal=None
        self.__tanggal_mulai=None
        self.__tanggal_selesai=None
        self.__tarif=None
        self.__total_bayar=None
        self.__status_bayar=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def kode_tempat(self):
        return self.__kode_tempat
        
    @kode_tempat.setter
    def kode_tempat(self, value):
        self.__kode_tempat = value
    @property
    def nomor_ktp(self):
        return self.__nomor_ktp
        
    @nomor_ktp.setter
    def nomor_ktp(self, value):
        self.__nomor_ktp = value
    @property
    def nomor_hp(self):
        return self.__nomor_hp
        
    @nomor_hp.setter
    def nomor_hp(self, value):
        self.__nomor_hp = value
    @property
    def nama_pelanggan(self):
        return self.__nama_pelanggan
        
    @nama_pelanggan.setter
    def nama_pelanggan(self, value):
        self.__nama_pelanggan = value
    @property
    def tanggal(self):
        return self.__tanggal
        
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value
    @property
    def tanggal_mulai(self):
        return self.__tanggal_mulai
        
    @tanggal_mulai.setter
    def tanggal_mulai(self, value):
        self.__tanggal_mulai = value
    @property
    def tanggal_selesai(self):
        return self.__tanggal_selesai
        
    @tanggal_selesai.setter
    def tanggal_selesai(self, value):
        self.__tanggal_selesai = value
    @property
    def tarif(self):
        return self.__tarif
        
    @tarif.setter
    def tarif(self, value):
        self.__tarif = value
    @property
    def total_bayar(self):
        return self.__total_bayar
        
    @total_bayar.setter
    def total_bayar(self, value):
        self.__total_bayar = value
    @property
    def status_bayar(self):
        return self.__status_bayar
        
    @status_bayar.setter
    def status_bayar(self, value):
        self.__status_bayar = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_tempat,self.__nomor_ktp,self.__nomor_hp,self.__nama_pelanggan,self.__tanggal,self.__tanggal_mulai,self.__tanggal_selesai,self.__tarif,self.__total_bayar,self.__status_bayar)
        sql="INSERT INTO Properti (kode_tempat,nomor_ktp,nomor_hp,nama_pelanggan,tanggal,tanggal_mulai,tanggal_selesai,tarif,total_bayar,status_bayar) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_tempat,self.__nomor_ktp,self.__nomor_hp,self.__nama_pelanggan,self.__tanggal,self.__tanggal_mulai,self.__tanggal_selesai,self.__tarif,self.__total_bayar,self.__status_bayar, id)
        sql="UPDATE properti SET kode_tempat = %s,nomor_ktp = %s,nomor_hp = %s,nama_pelanggan = %s,tanggal = %s,tanggal_mulai = %s,tanggal_selesai = %s,tarif = %s,total_bayar = %s,status_bayar = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByKODE_TEMPAT(self, kode_tempat):
        self.conn = mydb()
        val = (self.__nomor_ktp,self.__nomor_hp,self.__nama_pelanggan,self.__tanggal,self.__tanggal_mulai,self.__tanggal_selesai,self.__tarif,self.__total_bayar,self.__status_bayar, kode_tempat)
        sql="UPDATE properti SET nomor_ktp = %s,nomor_hp = %s,nama_pelanggan = %s,tanggal = %s,tanggal_mulai = %s,tanggal_selesai = %s,tarif = %s,total_bayar = %s,status_bayar = %s WHERE kode_tempat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM properti WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByKODE_TEMPAT(self, kode_tempat):
        self.conn = mydb()
        sql="DELETE FROM properti WHERE kode_tempat='" + str(kode_tempat) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM properti WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__kode_tempat = self.result[1]
        self.__nomor_ktp = self.result[2]
        self.__nomor_hp = self.result[3]
        self.__nama_pelanggan = self.result[4]
        self.__tanggal = self.result[5]
        self.__tanggal_mulai = self.result[6]
        self.__tanggal_selesai = self.result[7]
        self.__tarif = self.result[8]
        self.__total_bayar = self.result[9]
        self.__status_bayar = self.result[10]
        self.conn.disconnect
        return self.result
    def getByKODE_TEMPAT(self, kode_tempat):
        a=str(kode_tempat)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM properti WHERE kode_tempat='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__kode_tempat = self.result[1]
           self.__nomor_ktp = self.result[2]
           self.__nomor_hp = self.result[3]
           self.__nama_pelanggan = self.result[4]
           self.__tanggal = self.result[5]
           self.__tanggal_mulai = self.result[6]
           self.__tanggal_selesai = self.result[7]
           self.__tarif = self.result[8]
           self.__total_bayar = self.result[9]
           self.__status_bayar = self.result[10]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__kode_tempat = ''
           self.__nomor_ktp = ''
           self.__nomor_hp = ''
           self.__nama_pelanggan = ''
           self.__tanggal = ''
           self.__tanggal_mulai = ''
           self.__tanggal_selesai = ''
           self.__tarif = ''
           self.__total_bayar = ''
           self.__status_bayar = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM properti"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nomor_ktp FROM properti"
        self.result = self.conn.findAll(sql)
        return self.result