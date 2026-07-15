hours = int(input())
if hours <= 2:
    parkingfee = 0
else:
    if hours <= 5:
        parkingfee = (hours - 2) * 2
    else:
        parkingfee = (3 * 2) + (hours - 5) * 3
    if parkingfee > 30:
        parkingfee = 30
print(parkingfee)
 