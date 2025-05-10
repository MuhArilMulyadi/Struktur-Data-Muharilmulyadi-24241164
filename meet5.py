# program kalkulator sederhana
# (+ - x :)

operasi = input("anda ingin mengoperasikan apa? (+, -, *, /): ")
bil1 = float(input("masukan angka peratama: "))
bil2 = float(input("masukan angka kedua: "))

if operasi == "+":
    hasil = bil1 + bil2
elif operasi == "-":
    hasil = bil1 - bil2
elif operasi == "*":
    hasil = bil1 * bil2
elif operasi == "/":
      if bil2 != 0:
        hasil = bil1 / bil2
    else:
        hasil = "tidak bisa membagi dengan nol!"
else:
    hasil = "operasi tidak dikenali"
print("hasil:", hasil)
