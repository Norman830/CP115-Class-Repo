name = input()
price = float(input())
quantity = int(input())
member_answer = input()

order_total = price * quantity
is_member = bool (member_answer)
free_shipping = bool (order_total>100 + is_member)

print(name.upper())
print(order_total)
print(free_shipping)
print(is_member)
