class Kelvin:
 def __init__(self, suhu):
    self.suhu = suhu

 def get_kelvin(self):
    val = self.suhu
    return val

 def get_fahrenheit(self):
    val = (9/5 * (self.suhu - 273)) + 32
    return val

 def get_reamur(self):
    val = (4/5 * (self.suhu - 273))
    return val

 def get_celcius(self):
    val = self.suhu - 273
    return val

suhu = input("Masukkan suhu dalam kelvin:")
K = Kelvin(float (suhu))
val = K.get_kelvin()

F = K.get_fahrenheit()
R = K.get_reamur()
C = K.get_celcius()

print( str(val) + " Kelvin, sama dengan:")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(C) + " Celcius")