main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken":
    main_course = 10
elif main_course == "Beef":
    main_course = 12
else:
    main_course = 11

if drink == "Soft Drink":
    drink = 2
else:
    drink = 3

if dessert == "Ice Cream":
    dessert = 4
else:
    dessert = 5

total = main_course + drink + dessert
final_bill = total + (total * 0.10)

print(f"{final_bill:.2f}")
