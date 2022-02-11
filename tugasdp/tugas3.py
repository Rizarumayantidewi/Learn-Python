# masukkan hobi menggunakan user input list
#Tentukan variabel sebagai array
hobbies = []
#menjalankan kode
isInsert = 'R'

while(isInsert.lower() == 'r') :
	print('Masukkan Hobi kamu : ')
	newHobby = input()
	hobbies.append(newHobby)
	print('Isi lagi ? : [R/N] ')
	isInsert = input()

print ('Hobi saya adalah : ')
for index, hobby in enumerate(hobbies):
	print(f"{index + 1} {hobby}")