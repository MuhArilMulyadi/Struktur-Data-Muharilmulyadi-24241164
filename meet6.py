# Program Hak Akses Admin

# Input dari pengguna
username = input("Masukkan username: ")

# Cek hak akses
if username.lower() == "admin":
    print("Full akses diberikan.")
    # Aksi tambahan untuk admin (jika perlu)
    print("full akses.")
else:
    print("Akses denied.")
