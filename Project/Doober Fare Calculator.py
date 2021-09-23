Ride_type = “Black”
Credits = 4

Ride_price = 0
Final_price = 0

If ride_type == “DooberX”:
	Ride_price = 20.5
Elif ride_type == “Black”:
	Ride_price = 11.8
else:
	ride_price = 25.1

print(“Ride price:”)
print(ride_price)

if credits > 0:
	final_price = ride_price - credits

print(“Final price:”)
print(final_price)
