def straightline():
    hp = float(input("Masukkan Harga Perolehan (dalam Rupiah): "))
    nilaiResidu = float(input("Masukkan Nilai Residu: "))
    umur = float(input("Masukkan Umur Ekonomis (dalam tahun): "))
    depresiasi = (hp - nilaiResidu) / umur
    print("Hasil depresiasi menggunakan metode garis lurus adalah = Rp." + str(depresiasi))
    pilihan()


def servicehours():
    hp = float(input("Masukkan Harga Perolehan (dalam Rupiah): "))
    nilairesidu = float(input("Masukkan Nilai Residu: "))
    jamjasa = float(
        input("Masukkan taksiran waktu yang dapat digunakan mesin (dalam jam): "))
    depresiasi = (hp - nilairesidu) / jamjasa
    totalwaktu = float(
        input("Jumlah waktu yang telah digunakan mesin pada akhir periode (dalam jam): "))
    jml = depresiasi * totalwaktu
    print("Hasil nilai depresiasi menggunakan metode jam jasa adalah = Rp." + str(jml))
    pilihan()


def productiveoutput():
    hp = float(input("Masukkan Harga Perolehan (dalam Rupiah): "))
    nilairesidu = float(input("Masukkan Nilai Residu: "))
    hslproduksi = float(
        input("Masukkan taksiran hasil produksi yang dapat dilakukan oleh mesin: "))
    depresiasi = (hp - nilairesidu) / hslproduksi
    hasil = float(input("Jumlah unit produk yang dihasilkan mesin: "))
    total = depresiasi * hasil
    print("Hasil nilai depresiasi menggunakan metode taksiran hasil produksi adalah = Rp." + str(total))
    pilihan()


def sumofyears():
    hp = float(input("Masukkan Harga Perolehan (dalam Rupiah): "))
    nilairesidu = float(input("Masukkan Nilai Residu: "))
    umurekonomis = int(input("Masukkan umur ekonomis mesin (dalam tahun): "))
    jml = list(range(umurekonomis+1))
    jmlthn = sum(jml)
    sisaumur = (umurekonomis-1)
    depresiasi = (sisaumur / jmlthn) * (hp - nilairesidu)
    print("Hasil nilai depresiasi menggunakan metode jumlah angka tahun adalah = Rp." + str(depresiasi))
    pilihan()


def pilihan():
    print()
    lanjut = (input("Apakah akan lanjut? (y/t) : "))
    if lanjut == "y":
        return main()
    else:
        print("Program telah berhenti")
        exit()

# MAIN


def main():
    print("------------------------------------------")
    print("Program Menghitung Penyusutan Aktiva Tetap")
    print("------------------------------------------")
    print("Pilih metode yang akan digunakan:")
    print("1. Metode Garis Lurus")
    print("2. Metode Jam Jasa")
    print("3. Metode Hasil Produksi")
    print("4. Metode Jumlah Angka Tahun")
    print("5. Keluar")
    print()
    pilih = int(input("Masukkan Pilihan: "))
    if pilih == 1:
        straightline()
    elif pilih == 2:
        servicehours()
    elif pilih == 3:
        productiveoutput()
    elif pilih == 4:
        sumofyears()
    elif pilih == 5:
        print("Program telah berhenti")
        exit()
    else:
        print("error!")


main()
