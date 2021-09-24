bill = 25
tip_percentage = 0.11
tax_percentage = 0.008

tip = bill * tip_percentage
print(f"Tip: {tip}")

tax = bill * tax_percentage
print(f"Tax: {tax}")

total = bill + tip + tax
print(f"Total: {total}")