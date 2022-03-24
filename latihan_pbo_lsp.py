def garis():
    print("------------------------------")

#tampilan menu
print("------------------ Hotel Smk Jakarta Pusat 1 -------------------")
print("-- Lama Inap ----- Superior ------- Deluxe ------ Premium-")
print("- 1 s.d 2 Hari  - 100.000/Night- 150.000/Night - 200.000/Night -")
print("- 3 s.d 4 Hari  - 90.000/Night - 135.000/Night - 180.000/Night -")
print("- 5 Hari Keatas - 80.000/Night - 120.000/Night - 160.000/Night -")

#input data
tipe_kamar = input("Masukkan Tipe Kamar : ")
lama_inap = int(input("Masukkan Lama Menginap : "))



#tipe_superior
#jika memilih tipe superior
if tipe_kamar == "Superior":
    #jika lama menginap kurang atau sama dengan 2 hari
    if lama_inap <= 2:
        total_harga = 1000000*lama_inap
    #jika lama menginap kurang atau sama dengan 4 hari
    elif lama_inap <= 4:
        total_harga = 90000*lama_inap
    #jika lama menginap lebih dari 4 hari
    else:
        total_harga = 80000*lama_inap

#tipe_deluxe
#jika memilih tipe duluxe   
elif tipe_kamar == "Deluxe":
    #jika lama menginap kurang atau sama dengan 2 hari
    if lama_inap <= 2:
        total_harga = 150000*lama_inap
    #jika lama menginap kurang atau sama dengan 4 hari
    elif lama_inap <= 4:
        total_harga = 135000*lama_inap
    #jika lama menginap lebih dari 4 hari
    else:
        total_harga = 120000*lama_inap

#tipe_premium
#jika memilih tipe premium
elif tipe_kamar == "Premium":
    #jika lama menginap kurang atau sama dengan 2 hari
    if lama_inap <= 2:
        total_harga = 200000*lama_inap
    #jika lama menginap kurang atu sama dengan 4 hari
    elif lama_inap <= 4:
        total_harga = 180000*lama_inap
    #jika lama menginap lebih dari 4 hari
    else:
        total_harga = 160000*lama_inap

#total harga menginap
garis()
print("Tipe Kamar Yang Dipilih : ", (tipe_kamar))
print("Lama Menginap : ", (lama_inap), "Hari")
print("Total Harga Yang Dibayar : Rp. ", (total_harga))

