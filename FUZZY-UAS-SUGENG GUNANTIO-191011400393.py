print('NAMA : SUGENG GUNANTIO\nKELAS : 06TPLE007\nUAS KECERDASAN BUATAN : FUZZY\n')

rasaMakanan = float(input("Masukkan nilai rasa makanan = "))
fasilitas = float(input("Masukkan nilai Fasilitas = "))
harga = float(input("Masukkan nilai harga = "))

# nilai xmax
xmax_rasaMakanan = 15
xmax_fasilitas = 20
xmax_harga = 10
xmax_hasil = 5

# nilai xmin
xmin_rasaMakanan = 5
xmin_fasilitas = 10
xmin_harga = 4
xmin_hasil = 1

# true  = Enak
# false = Biasa
kondisi_rasaMakanan = bool

# true =  Lengkap
# false = Tidak Lengkap
kondisi_fasilitas = bool

# true = Mahal
# false = Murah
kondisi_harga = bool

# true = Bagus
# false = Sedang
kondisi_hasil = bool


def cek_rasaMakanan(cek_rasaMakanan):
    if 5 <= cek_rasaMakanan < 10:
        kondisi_rasaMakanan = False
        # print(kondisi_rasaMakanan)
    elif cek_rasaMakanan >= 10 and cek_rasaMakanan <= 15:
        kondisi_rasaMakanan = True
        # print(kondisi_rasaMakanan)
    return kondisi_rasaMakanan

def cekFasilitas(cek_fasilitas):
    if 10 <= cek_fasilitas < 15:
        kondisi_fasilitas = False
        # print(kondisi_fasilitas)
    elif cek_fasilitas >= 15 and cek_fasilitas <= 20:
        kondisi_fasilitas = True
        # print(kondisi_fasilitas)
    return kondisi_fasilitas

def cekHarga(cek_harga):
    if 4 <= cek_harga < 7:
        kondisi_harga = False
        # print(kondisi_harga)
    elif cek_harga >= 7 and cek_harga <= 10:
        kondisi_harga = True
        # print(kondisi_harga)
    return kondisi_harga

def cekHasil(cek_hasil):
    if 1 <= cek_hasil < 3:
        kondisi_hasil = False
        # print(kondisi_hasil)
    elif cek_hasil >= 3 and cek_hasil <= 5:
        kondisi_hasil = True
        # print(kondisi_hasil)
    return kondisi_hasil

# cek_rasaMakanan(25)
cek_kk = cek_rasaMakanan(rasaMakanan)
cek_f = cekFasilitas(fasilitas)
cek_h = cekHarga(harga)

# mendekatiKiri
def mendekatiKiri(xmax, xmin, x):
    hasil_ke_kiri = (xmax - x) / (xmax - xmin)
    return hasil_ke_kiri

def mendekatiKanan(xmax, xmin, x):
    hasil_ke_kanan = (x-xmin) / (xmax-xmin)
    return hasil_ke_kanan


kiri_kk = mendekatiKiri(xmax_rasaMakanan, xmin_rasaMakanan, rasaMakanan)
kanan_kk = mendekatiKanan(xmax_rasaMakanan, xmin_rasaMakanan, rasaMakanan)

kiri_fasilitas = mendekatiKiri(xmax_fasilitas, xmin_fasilitas, fasilitas)
kanan_fasilitas = mendekatiKanan(xmax_fasilitas, xmin_fasilitas, fasilitas)

kiri_harga = mendekatiKiri(xmax_harga, xmin_harga, harga)
kanan_harga = mendekatiKanan(xmax_harga, xmin_harga, harga)


# def cek(kondisi_rasaMakanan , kondisi_fasilitas , kondisi_harga  )
# print(cek_kk)
# print(cek_f)
# print(cek_h)
# print(kiri_kk)
# print(kiri_fasilitas)
# print(kiri_harga)

if cek_kk == False and cek_f == False and cek_h == False:
    alfa = min(kiri_kk, kiri_fasilitas, kiri_harga)
    hasil = xmin_hasil +  (alfa*(xmax_hasil-xmin_hasil))
    print("")
    print("Jawaban ")
    print("")
    print("Nilai dari hasil = " , hasil )
    kondisi = cekHasil(hasil)
    if kondisi:
        print("Hasil = Bagus")
    else:
        print("hasil = Sedang")

elif cek_kk == False and cek_f == False and cek_h == True:
    alfa = min(kiri_kk, kiri_fasilitas, kanan_harga)
    hasil = xmax_hasil -  (alfa*(xmax_hasil-xmin_hasil))
    # print(hasil)
    # cekHasil(hasil)
    print("")
    print("Jawaban ")
    print("")
    print("Nilai dari hasil = " , hasil )
    kondisi = cekHasil(hasil)
    if kondisi:
        print("Hasil = Bagus")
    else:
        print("hasil = Sedang")
elif cek_kk == False and cek_f == True and cek_h == False:
    alfa = min(kiri_kk, kanan_fasilitas, kiri_harga)
    hasil = xmax_hasil -  (alfa*(xmax_hasil-xmin_hasil))
    # print(hasil)
    # cekHasil(hasil)
    print("")
    print("Jawaban ")
    print("")
    print("Nilai dari hasil = " , hasil )
    kondisi = cekHasil(hasil)
    if kondisi:
        print("Hasil = Bagus")
    else:
        print("hasil = Sedang")
elif cek_kk == False and cek_f == True and cek_h == True:
    alfa = min(kiri_kk, kanan_fasilitas, kanan_harga)
    hasil = xmax_hasil -  (alfa*(xmax_hasil-xmin_hasil))
    # print(hasil)
    # cekHasil(hasil)
    print("")
    print("Jawaban ")
    print("")
    print("Nilai dari hasil = " , hasil )
    kondisi = cekHasil(hasil)
    if kondisi:
        print("Hasil = Bagus")
    else:
        print("hasil = Sedang")
elif cek_kk == True and cek_f == False and cek_h == False:
    alfa = min(kanan_kk, kiri_fasilitas, kiri_harga)
    hasil = xmin_hasil +  (alfa*(xmax_hasil-xmin_hasil))
    # print(hasil)
    # cekHasil(hasil)
    print("")
    print("Jawaban ")
    print("")
    print("Nilai dari hasil = " , hasil )
    kondisi = cekHasil(hasil)
    if kondisi:
        print("Hasil = Bagus")
    else:
        print("hasil = Sedang")
elif cek_kk == True and cek_f == False and cek_h == True:
    alfa = min(kanan_kk, kiri_fasilitas, kanan_harga)
    print(alfa)
    hasil = xmin_hasil + (alfa*(xmax_hasil-xmin_hasil))
    # print(hasil)
    # cekHasil(hasil)
    print("")
    print("Jawaban ")
    print("")
    print("Nilai dari hasil = " , hasil )
    kondisi = cekHasil(hasil)
    if kondisi:
        print("Hasil = Bagus")
    else:
        print("hasil = Sedang")
elif cek_kk == True and cek_f == True and cek_h == False:
    alfa = min(kanan_kk, kanan_fasilitas, kiri_harga)
    hasil = xmax_hasil -  (alfa*(xmax_hasil-xmin_hasil))
    # print(hasil)
    # cekHasil(hasil)
    print("")
    print("Jawaban ")
    print("")
    print("Nilai dari hasil = " , hasil )
    kondisi = cekHasil(hasil)
    if kondisi:
        print("Hasil = Bagus")
    else:
        print("hasil = Sedang")
elif cek_kk == True and cek_f == True and cek_h == True:
    alfa = min(kanan_kk, kanan_fasilitas, kiri_harga)
    hasil = xmax_hasil -  (alfa*(xmax_hasil-xmin_hasil))
    # print(hasil)
    # cekHasil(hasil)
    print("")
    print("Jawaban ")
    print("")
    print("Nilai dari hasil = " , hasil )
    kondisi = cekHasil(hasil)
    if kondisi:
        print("Hasil = Bagus")
    else:
        print("hasil = Sedang")