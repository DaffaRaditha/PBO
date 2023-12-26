print("Konversi Suhu Kelvin")
def get_fahrenheit(suhu):
    F = (9/5 * (float(suhu) - 273)) + 32
    return F

def get_reamur(suhu):
    R = 4/5 * (float(suhu) - 273)
    return R

def get_celcius(suhu):
    C = float(suhu) - 273
    return C

# Entry
suhu = input("Masukkan suhu dalam Kelvin:")

# rumus
F = get_fahrenheit(suhu)
R = get_reamur(suhu)
C = get_celcius(suhu)

#output
print(suhu + " Kelvin sama dengan ")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(C) + " Celcius")