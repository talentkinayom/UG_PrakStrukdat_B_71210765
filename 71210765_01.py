x = True
while x:
    print('Pilihan:\n1.Perjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\nQ.Keluar')
    operator = (input('Masukkan pilihan: '))
    if operator == "1":
        bil1 = int(input('Masukkan bilangan 1: '))
        bil2 = int(input('Masukkan bilangan 2: '))
        hasil = bil1 + bil2
        print('Hasil dari ', bil1,' + ',bil2,' = ',hasil)
    elif operator == "2":
        bil1 = int(input('Masukkan bilangan 1: '))
        bil2 = int(input('Masukkan bilangan 2: '))
        hasil = bil1 - bil2
        print('Hasil dari ', bil1,' - ',bil2,' = ',hasil)
    elif operator == "3":
        bil1 = int(input('Masukkan bilangan 1: '))
        bil2 = int(input('Masukkan bilangan 2: '))
        hasil = bil1 * bil2
        print('Hasil dari ', bil1,' * ',bil2,' = ',hasil)
    elif operator == "4":
        bil1 = int(input('Masukkan bilangan 1: '))
        bil2 = int(input('Masukkan bilangan 2: '))
        hasil = bil1 / bil2
        print('Hasil dari ', bil1,' / ',bil2,' = ',hasil)
    elif operator == "Q":
        x = False
