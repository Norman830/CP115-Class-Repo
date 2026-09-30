'''
Programmer's name: Norman Danish Bin Rajimin Class: C01 
Creating a discount calculator for PASU Telecommunication Company monthly mobile line bill
'''

monthly_use = float(input("Enter Monthly Usage:RM")) #asks for the raw monthly bill before discount

if monthly_use < 0 :        #check if the input is a real number
    print("Invalid Input")  
else:
    if monthly_use < 50:    #not eligible for any discount
        discount = 0
    elif monthly_use >= 50 and monthly_use <= 100:  #eligible for 5% discount
        discount = 0.05
    else:                   #eligible for 20% discount because bill is over 100
        discount = 0.20

    final_bill = monthly_use - (monthly_use * discount) #calculate total bill to be paid after discount
    print (f"Bills to be paid: {final_bill:.2f}")        #prints the bill to be paid :)