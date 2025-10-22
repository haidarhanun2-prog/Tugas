gaji_pokok = 300000
nama = input("Nama Karyawan : ")
Golongan = input("Golongan Jabatan 1/2/3 : ")
Pendidikan = input("Pendidikan SMA/D1/D3/S1 : ")
Jumlah_jam = int(input("Jumlah Jam Kerja : "))

if Golongan == "1":
    tunjangan_gol = gaji_pokok*(5/100)
elif Golongan == "2":
    tunjangan_gol = gaji_pokok*(10/100)
elif Golongan == "3":
    tunjangan_gol = gaji_pokok*(15/100)
else:
    tunjangan_gol = 0

if Pendidikan == "SMA" or Pendidikan == "sma":
    tunjangan_pen = gaji_pokok*(2.5/100)
elif Pendidikan == "D1" or Pendidikan == "d1":
    tunjangan_pen = gaji_pokok*(5/100)
elif Pendidikan == "D3" or Pendidikan == "d3":
    tunjangan_pen = gaji_pokok*(20/100)
elif Pendidikan == "S1" or Pendidikan == "s1":
    tunjangan_pen = gaji_pokok*(30/100)
else:
    tunjangan_pen = 0

if Jumlah_jam >8:
    honor_lem = (Jumlah_jam-8)*3500
else:
    honor_lem = 0

total_gaji = gaji_pokok+tunjangan_pen+tunjangan_gol+honor_lem
print(" ")
print("Honor Yang Diterima")
print("Nama Karyawan : ",nama)
print("Tunjangan Jabatan : ","Rp.",int(tunjangan_gol))
print("Tunjangan Pendidikan : ","Rp.",int(tunjangan_pen))
print("Honor Lembur : ","Rp.",honor_lem)
print("Total gaji : ","Rp.",int(total_gaji))