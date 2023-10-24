print("Menghitung Luas Dan Volume Prisma Segitiga")

# Nilai
alas = 7
tinggi_segitiga = 5
tinggi_prisma = 10

# Rumus
luas_selimut = (alas + alas + alas) * tinggi_prisma
luas_permukaan = luas_selimut + alas * tinggi_segitiga
volume = 0.5 * alas * tinggi_segitiga * tinggi_prisma

# Output
print("Alas = ", alas)
print("Tinggi Segitiga = ", tinggi_segitiga)
print("Tinggi Prisma = ", tinggi_prisma)
print("Luas Selimut = ", luas_selimut)
print("Luas Permukaan = ", luas_permukaan)
print("Volume = ", volume)
