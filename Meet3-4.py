print("Apakah Anda ingin menghitung luas persegi atau segitiga?")
pilihan = input("Masukkan 'persegi' atau 'segitiga': ").lower()

if pilihan == "persegi":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print("Luas = ", luas)

elif pilihan == "segitiga":
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Luas = ", luas)

else:
    print("Pilihan tidak valid. Silakan masukkan 'persegi' atau 'segitiga'.")