upper_limit = 88
lower_limit = 11
outlier = False
number = 25

if number > upper_limit:
    outlier = True
if number < lower_limit:
    outlier = True
if outlier == True:
    print(f"{number} is an outlier")