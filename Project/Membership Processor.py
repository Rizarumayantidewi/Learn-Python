name_box = "Riza Rumayanti Dewi"
age_box = "18"
uni_box = ""
subs_box = "1.88"
mkt_box = "0"

name_entered = bool(name_box)
if name_entered:
    name = name_box
else:
    name = "Unknown"

age = int(age_box)
student = bool(uni_box)
subscription = float(subs_box)
marketing = bool(int(mkt_box))

profile = name + ',' + str(age)
print(profile)