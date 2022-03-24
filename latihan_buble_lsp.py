#membuat garis
def garis():
    print("----------------------")

#fungsi bubble sort ascending (dari kecil ke besar)
def sort_asc(array):
    array = sorted(array)
    return(array)

#fungsi bubble sort descending (dari besar ke kecil)
def sort_desc(array):
    array = sorted(array, reverse = True)
    return(array)
    

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka) /len(angka)

#input nilai
garis()
print("Masukan Tiga Buah Nilai")

#masukan tipe data integer
nilai_a = int(input("Nilai A : "))
nilai_b = int(input("NIlai B : "))
nilai_c = int(input("Nilai C : "))
angka = [nilai_a, nilai_b, nilai_c]
garis()
print()

#nilai akhir
print("Hasil Akhir :p")
print("Urutan Angka Ascending : ",(sort_asc(angka)))
print("Urutan Angka Descending : ",(sort_desc(angka)))

#angka terbesar
print("Angka Terbesar : ", max(angka))

#angka terkecil
print("Angka Terkecil : ", min(angka))

#rata-rata
print("Rata-ratanya : ", round(rata_rata(angka),2))
