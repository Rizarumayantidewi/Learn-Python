import time
from functools import reduce

#Global Variabel
currentYear = int(time.strftime ('%Y'))
userData = []

#Get Age Function
getAge = lambda born : abs (currentYear - born)

#input from console
inputNewData = 'Y'
while(inputNewData.lower() == 'y') :
	userObjek = {}
	print('Masukkan nama :')
	userObjek ['name'] = input ()
	print ('Masukkan tahun lahir : ')
	userObjek['born'] = int(input())
	userData.append (userObjek)
	userObjek = {}
	print ('Ingin menambah user? [Y/N]')
	inputNewData = input ()

#Filter user by youngest
userData = sorted (userData, key= lambda x : getAge (x['born']), reverse= True)
#Find user by oldest
olderUser = reduce(lambda x, y : x if getAge (x ['born']) > getAge (y['born']) else y, userData)


#print result to console
print ("\n\n====================\n")
print (f"{olderUser ['name']} adalah orang paling tua dengan umur {getAge (olderUser ['born'])} tahun")
print ("====================")

#Compare oldest user with another user
for index, user in enumerate (userData) :
	if user ['name'] != olderUser ['name'] :
		print (f"No : {index}")
		print (f"Nama : {user['name']}")
		print (f"Perbedaan umur : {abs(getAge(user ['born']) - getAge(olderUser['born']))} tahun")
		print ("====================")