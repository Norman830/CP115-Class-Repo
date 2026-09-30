position = input()
overtime_hours = int(input())
is_weekend = input()

if position == "Manager":
    if is_weekend == "yes":
        if overtime_hours <= 8:
            overtime_pay = ((30 * 1.5) *  overtime_hours) + (overtime_hours * 5)
        else:
            overtime_pay = ((30 * .20 *  overtime_hours) + (overtime_hours * 5)



print(overtime_pay)
