class karyawan:
    jumlah_karyawan = 0
 
    def __init__(self, nama, gaji, umur):
        self.nama = nama
        self.gaji = gaji
        self.umur = umur
        karyawan.jumlah_karyawan += 1
 
    def tampilkan_jumlah(self):
        print("Total karyawan:", karyawan.jumlah_karyawan)
 
    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji, "perhari")
        print("Umur :", self.umur)
        print("-----------")
 
karyawan1 = karyawan("Budi", 600000, 25)
karyawan2 = karyawan("Bambang", 550000, 22)
 
karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan :", karyawan.jumlah_karyawan)