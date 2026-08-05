item_name = input("Enter the name of the item: ")
item_price = float(input("Enter the price of the item: "))
item_quantity = int(input("Enter the quantity of the item: "))
subtotal = item_price * item_quantity
aftertax = subtotal * 0.06
total_cost = subtotal + aftertax
print (f"The subtotal is RM {subtotal} with a tax of RM {aftertax} or 6%, making the total cost RM {total_cost}.")