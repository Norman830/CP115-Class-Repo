coffee = int(input("coffee:"))
muffin = int(input("muffin:"))
water = int(input("water:"))

tcoffee = coffee * 3.50	
tmuffin = muffin  * 2.10
twater = water * 1.05
subtotal = tcoffee + tmuffin + twater 
tax = subtotal *0.06
finaltotal = tax + subtotal

print(f"========== RECEIPT ==========\n"
      f"Item\tPrice\tQty\tTotal\n"
      f"Coffee\t$3.50\t{coffee}\t{tcoffee:.2f}\n"
      f"muffin\t$2.10\t{muffin}\t{tmuffin:.2f}\n"
      f"water\t$1.05\t{water}\t{twater:.2f}\n"
      f"------------------------------\n"
      f"Subtotal\t\t{subtotal:.2f}\n"
      f"Tax(6%)\t\t\t{tax:.2f}\n"
      f"Total\t\t\t{finaltotal:.2f}") 