UserData = {}
inputNewUser = 'Y'

while(inputNewUser.lower() == 'y') :
	#input from compile
	print ('Masukkan data nama pengguna : ')
	userName = input ()
	print ('Masukkan data umur pengguna : ')
	userAge = int (input () )
	#assign to object
	UserData[userName] = userAge

	#promp need reinput
	print ('Masukkan data lagi ? [Y/N] ')
	inputNewUser = input ()

#output

print ("\n========== Output ========== \n")
loopIndex = 0
for key, value in UserData.items() :
	loopIndex += 1
	print (f"{ loopIndex }. Orang dengan nama { key } ")
	print (f"{ loopIndex }. Berumur { value } tahun")
	print ("\n=========================\n")


