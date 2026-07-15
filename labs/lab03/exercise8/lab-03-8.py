principal = int(input())
rate = int(input())
time = int(input())
interest = float(principal * rate * time) / 100
print(interest)
totalAmount = principal + interest
print(totalAmount)
monthlyInterest = float(interest) / time * 12
print(monthlyInterest)
 