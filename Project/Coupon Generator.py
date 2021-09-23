base = "www.RizaRumayantiDewi.com"
coupon = "signup/coupon"
discount = 11
amount = 8


for num in range(amount):
    print(f"{base}/{coupon}/{discount}/{num}")

print(f"{amount} coupons created")