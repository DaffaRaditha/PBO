print("Konversi Suhu Fahrenheit")
def get_reamur(suhu):
    R = 4/9 * (float(suhu) - 32)
    return R

def get_kelvin(suhu):
    K = (5/9 * (float(suhu) - 32)) + 273
    return K

def get_celcius(suhu):
    C = 5/9 * (float(suhu) - 32)
    return C

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit:")

# rumus
R = get_reamur(suhu)
K = get_kelvin(suhu)
C = get_celcius(suhu)

#output
print(suhu + " Fahrenheit sama dengan ")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
print(str(C) + " Celcius")