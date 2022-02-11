'''program untuk menghitung umur'''

#nama pengguna
nama =raw_input ("siapakah anda?")
  

#tanggal lahir dari pengguna semuanya dalam angka
tlahir = input ("tanggal kelahiran")
blahir = input ("bulan kelahiran")
dlahir = input ("tahun kelahiran")
lahir = tlahir + (blahir * 30) + (dlahir * 365)

#tanggal aktual
taktual = input ("tanggal saat ini")
baktual = input ("bulan saat ini")
daktual = input ("tahun saat ini")
aktual = taktual + (baktual * 30) + (daktual * 365)

#memulai proses kalkulasi
tahun = (aktual - lahir) / 365
bulan = ((aktual - lahir) % 365) / 30
hari = ((aktual - lahir) % 365) % 30

#tampilkan hasil
print "Bonjour!", nama, "anda berumur :",
print hari, "hari", bulan, "bulan", tahun, "tahun"

'''tambahan untuk komentar'''
if tahun <= 5:
    print"anda masih balita"
elif tahun <= 17:
    print "anda masih remaja"
elif tahun <= 45:
        print "anda sudah dewasa"
elif tahun <= 99:
    print "anda sudah tua"
else :
                "anda keterlaluan"