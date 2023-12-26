print("Konversi Suhu Reamur")

# Entry
suhu = input("Masukkan suhu dalam Reamur:")


# rumus
F = (9/4 * float(suhu)) + 32
K = (5/4 * float(suhu)) + 273
C = 5/4 * float(suhu)

#output
print(suhu + " Reamur sama dengan ")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")
print(str(C) + " Celcius")