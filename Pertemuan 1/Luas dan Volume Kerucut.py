print("Menghitung Luas Dan Volume Kerucut")

# Nilai
jari_jari = 3
tinggi = 5
garis_pelukis = 7

# Rumus
luas_selimut = 3.14 * jari_jari * garis_pelukis
luas_permukaan = luas_selimut + 3.14 * jari_jari**2
volume = (1/3) * 3.14 * jari_jari**2 * tinggi

# Output
print("Jari-jari = ", jari_jari)
print("Tinggi = ", tinggi)
print("Garis Pelukis = ", garis_pelukis)
print("Luas Selimut = ", luas_selimut)
print("Luas Permukaan = ", luas_permukaan)
print("Volume = ", volume)
