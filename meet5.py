# program kalkulator sederhana
# (+ - x :)

operasi = input("anda ingin mengoprasikan apa? (+, -, *, /) ")
bil1 = float(input("masukan angka pertama: "))
bil2 = float(input("masukan angka kedua: "))

 if operasi == "+" :
     final = bil1 + bil2
     print(final)
elif operasi == "-" :
    final = bil1 - bil2
    print(final)
elif operasi == "x" : 
    final = bil1 * bil2
    print(final)
else :
    final bil1 / bil2
    print(final)