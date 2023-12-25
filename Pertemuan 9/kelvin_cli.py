print("Konversi Suhu Kelvin")

# Entry
suhu = input("Masukkan suhu dalam Kelvin:")


# rumus
F = (9/5 * (float(suhu) - 273)) + 32
R = (4/5 * (float(suhu) - 273))
C = float(suhu) - 273

#output
print(suhu + " kelvin sama dengan ")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(C) + " Celcius")