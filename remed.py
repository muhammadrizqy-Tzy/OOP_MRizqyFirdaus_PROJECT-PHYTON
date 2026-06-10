kapasitas = 100
total = 0

while total < kapasitas:
    datang = int(input("Peserta datang: "))
    total = total + datang

print("Seminar penuh")
print("Total peserta:", total)