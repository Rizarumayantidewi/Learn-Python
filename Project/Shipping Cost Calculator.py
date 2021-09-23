International_shipping = True

Total = 180
Shipping_cost = 0

If international_shipping:
	Shipping_cost += 11
	Print(“International base cost applied”)

If total <= 50:
	Shipping_cost += 25
Elif total <= 100:
	Shipping_cost += 88
Else:
	Shipping_cost += 8

Print(f”Shipping cost: {shipping_cost}”)
