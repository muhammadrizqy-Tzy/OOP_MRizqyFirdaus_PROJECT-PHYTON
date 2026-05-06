# Meminta input dari pengguna dalam stasiun kbps
kbps = float(input("kategori kecepatan internet(mbps): "))
mbps =kbps/1000


if mbps > 50:
 kategori = "sangat cepat"
elif mbps > 20:
 kategori = "cepat"
elif mbps > 5:
 kategori = "sedang"
else:
 kategori = "lambat"
 
# Menampilkan hasil keputusan
print("kecepatan", mbps,"mbps")
print("kategori:", kategori)
