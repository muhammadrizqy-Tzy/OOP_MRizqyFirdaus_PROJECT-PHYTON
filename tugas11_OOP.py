nilai = [80, 75, 90, 85, 95, 88, 70, 92, 87, 89]
tertinggi = nilai[0]
for data in nilai:
    if data > tertinggi:
        tertinggi = data
print("Nilai tertinggi =", tertinggi)