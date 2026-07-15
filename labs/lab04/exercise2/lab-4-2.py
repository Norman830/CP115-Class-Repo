income = int(input())
if income <= 50000:
    toaltax = income * 0
else:
    if income <= 100000:
        totaltax = (income - 50000) * 1 / 100
    else:
        totaltax = (50000 * 1 / 100) + (income - 100000) * 2 / 100
print(totaltax)
