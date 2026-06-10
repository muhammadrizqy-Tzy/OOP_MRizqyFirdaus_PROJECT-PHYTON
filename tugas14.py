total =0
while true:
    harga = int(input("Masukkan harga barang (0 untuk selesai): "))
    if harga == 0:
        break
        
   total += harga:
if total >= 50000:
    total -= 5000
    print("Anda mendapatkan diskon Rp5.000!")
print(f"Total yang harus dibayar: Rp{total}")
