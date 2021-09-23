account = 100
interest_rate = 0.008
years = 8

print(f"Initial amount: {account}")

counter = 1
while counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f"year {counter}: {account}")
    counter += 1