# Program sederhana untuk menampilkan nama dan NIM 6 anggota kelompok
 
#Nama kelokpok
#Nama Ketua: Muh aril mulyadi (24241164)
#Nama Anggota: afrizan hidayat (24241188)
#Nama Anggota: pawaiz (24241170)
#Nama Anggota: m.fathir al fariz (24241161)
#Nama Anggota: Eka putra gilang ramadhan (24241166)
#Nama Anggota: riska safitri (24241173)

# Input nama dan NIM dari 6 anggota kelompok
nama1 = input("Masukkan nama anggota 1: ")
nim1 = input("Masukkan NIM anggota 1: ")
nama2 = input("Masukkan nama anggota 2: ")
nim2 = input("Masukkan NIM anggota 2: ")
nama3 = input("Masukkan nama anggota 3: ")
nim3 = input("Masukkan NIM anggota 3: ")
nama4 = input("Masukkan nama anggota 4: ")
nim4 = input("Masukkan NIM anggota 4: ")
nama5 = input("Masukkan nama anggota 5: ")
nim5 = input("Masukkan NIM anggota 5: ")
nama6 = input("Masukkan nama anggota 6: ")
nim6 = input("Masukkan NIM anggota 6: ")

# Menampilkan hasil
print("\nDaftar Anggota Kelompok dan NIM:")
print(f"1. {nama1} - {nim1}")
print(f"2. {nama2} - {nim2}")
print(f"3. {nama3} - {nim3}")
print(f"4. {nama4} - {nim4}")
print(f"5. {nama5} - {nim5}")
print(f"6. {nama6} - {nim6}")

# Operasi aritmatika sederhana
total_karakter_nama = len(nama1) + len(nama2) + len(nama3) + len(nama4) + len(nama5) + len(nama6)
total_karakter_nim = len(nim1) + len(nim2) + len(nim3) + len(nim4) + len(nim5) + len(nim6)

# Menampilkan total karakter nama
print(f"\nTotal karakter nama semua anggota: {total_karakter_nama}")
print(f"\nTotal karakter nim semua anggota:{total_karakter_nim}")

# Komparasi/logika sederhana
if total_karakter_nama > 50:
    print("Total karakter nama lebih dari 50")
else:
    print("Total karakter nama kurang dari atau sama dengan 50")
if total_karakter_nim > 50:
    print("Total karakter nim lebih dari 50")
else:
    print("Total karakter nim kurang dari atau sama dengan 50")