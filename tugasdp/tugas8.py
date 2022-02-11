import time

# Define current year 
currentYear = int (time.strftime ('%Y'))

# input
print ('Masukkan tahun lahir : ')
loopYear = int (input (':'))

# loop years
while loopYear <= currentYear:
	print (f"Tahun { loopYear } \n")
	loopYear += 1