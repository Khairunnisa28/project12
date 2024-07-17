import math

def menu():
    print("Pilih bangun datar yang ingin dihitung:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Keluar")

def persegi():
    sisi = float(input("Masukkan panjang sisi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    print(f"Luas Persegi: {luas}")
    print(f"Keliling Persegi: {keliling}")

def persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print(f"Luas Persegi Panjang: {luas}")
    print(f"Keliling Persegi Panjang: {keliling}")

def segitiga():
    alas = float(input("Masukkan panjang alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    sisi1 = float(input("Masukkan panjang sisi 1: "))
    sisi2 = float(input("Masukkan panjang sisi 2: "))
    sisi3 = float(input("Masukkan panjang sisi 3: "))
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    print(f"Luas Segitiga: {luas}")
    print(f"Keliling Segitiga: {keliling}")

def lingkaran():
    jari_jari = float(input("Masukkan panjang jari-jari: "))
    luas = math.pi * jari_jari * jari_jari
    keliling = 2 * math.pi * jari_jari
    print(f"Luas Lingkaran: {luas}")
    print(f"Keliling Lingkaran: {keliling}")

while True:
    menu()
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
    
    if pilihan == '1':
        persegi()
    elif pilihan == '2':
        persegi_panjang()
    elif pilihan == '3':
        segitiga()
    elif pilihan == '4':
        lingkaran()
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
