import time

currentYear = int(time.strftime('%Y'))

# Program sederhana menghitung umur
print ("Nama teman saya Muhammad Kevyn Tubagus")
print (f"{ currentYear - 2000 } tahun")

print ("Nama saya Riza Rumayanti Dewi")
print (f"{ currentYear - 2002 } tahun")

#Selisih umur saya dan teman saya
print("\v \v" "_______________________________________\v")
print("selisih kami")
c = 20 - 18
print (c), print ("\t tahun")

#Pembuktian
print("\v" "_______________________________________\v")
print ((currentYear - 2000) == (currentYear - 2002))

#Maka
d = 2
print ("Umur kami sama" if d < 0 else "Umur kami berbeda")
