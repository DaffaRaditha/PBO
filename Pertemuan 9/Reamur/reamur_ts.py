print("Konversi Suhu Reamur")
def get_fahrenheit(suhu):
    F = (9/4 * float(suhu)) + 32
    return F

def get_kelvin(suhu):
    K = (5/4 * float(suhu)) + 273
    return K

def get_celcius(suhu):
    C = 5/4 * float(suhu)
    return C

# Entry
suhu = input("Masukkan suhu dalam Reamur:")

# rumus
F = get_fahrenheit(suhu)
K = get_kelvin(suhu)
C = get_celcius(suhu)

#output
print(suhu + " Reamur sama dengan ")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")
print(str(C) + " Celcius")