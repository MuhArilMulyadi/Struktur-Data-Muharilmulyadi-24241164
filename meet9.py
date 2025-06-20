# Meminta input dari pengguna
domain = input("Masukkan nama domain Anda: ")

# Mengecek jumlah bagian setelah dipisah dengan titik
bagian = domain.split(".")

if len(bagian) == 1:
    print("Input terdeteksi hanya sebagai ekstensi:", bagian[0])
elif len(bagian) == 2:
    print("Nama domain:", bagian[0])
    print("Ekstensi domain:", bagian[1])
else:
    print("Subdomain:", ".".join(bagian[:-2]))
    print("Nama domain:", bagian[-2])
    print("Ekstensi domain:", bagian[-1])

