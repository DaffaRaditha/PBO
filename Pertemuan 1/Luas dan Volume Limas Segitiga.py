print("Menghitung Luas Dan Volume Limas Segitiga")

# Nilai
alas = 7
tinggi_segitiga = 5
tinggi_limas = 10

# Rumus
luas_alas = 0.5 * alas * tinggi_segitiga
luas_sisi_tegak = 3 * (0.5 * alas * tinggi_limas)
luas = luas_alas + luas_sisi_tegak
volume = (1/6) * alas * tinggi_segitiga * tinggi_limas

# Output
print("Alas = ", alas)
print("Tinggi Segitiga = ", tinggi_segitiga)
print("Tinggi Limas = ", tinggi_limas)
print("Luas = ", luas)
print("Volume = ", volume)
