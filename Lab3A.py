currentBalance = float(input("Amount owed: $"))
apr = float(input("APR: "))
mpr = round(apr / 12,3)
print(f"Monthly percentage rate: {mpr:.3f}")
minPay = (currentBalance * mpr)/100
print(f"Minimum payment: $ {minPay:.2f}")