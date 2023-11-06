print("Menghitung Luas Dan Volume Silinder (Tabung)")

# Nilai
jari_jari = 5
tinggi = 10

# Rumus
luas_selimut = 2 * 3.14 * jari_jari * tinggi
luas_permukaan = luas_selimut + 2 * 3.14 * jari_jari**2
volume = 3.14 * jari_jari**2 * tinggi

# Output
print("Jari-jari = ", jari_jari)
print("Tinggi = ", tinggi)
print("Luas Selimut = ", luas_selimut)
print("Luas Permukaan = ", luas_permukaan)
print("Volume = ", volume)
