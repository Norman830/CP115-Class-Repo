weight = int(input())
ticketprice = int(input())
if weight > 15:
    finalprice = (weight - 15) * 4 + ticketprice
else:
    if weight == 0:
        finalprice = ticketprice - 10
    else:
        finalprice = ticketprice
print(finalprice)
