
print("Welcome to the tip calculator!")
charge_food=float(input('Please enter the charge for the food : '))
tip_amount=(charge_food*18/100) # Tip amount in %
sales_tax=(charge_food*7/100) # sales tax amount in %
Grand_total=(charge_food + tip_amount + sales_tax) #display the charge of the food plus tip and sales tax.
print(f"Tip paid: ${tip_amount}")
print(f"The total Sales tax: ${sales_tax}")
print(f"The grand total amount paid: ${Grand_total}")