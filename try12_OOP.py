# CONTOH STRUKTUR PERCABANGAN IF
# Input data dari pengguna
nilai_ujian = float(input("masukan nilai ujian siswa: "))

# Struktur Kontrol percabangan majemuk
if nilai_ujian >= 90:
 predikat = "sangat baik (A)"
elif nilai_ujian >= 75:
 predikat = "baik (B)"
elif nilai_ujian >= 60:
 predikat = "cukup (C)"
else:
 predikat = "kurang (D) - memerlukan remedial"
 
# Menampilkan hasil keputusan
print("hasil evaluasi:", predikat)
