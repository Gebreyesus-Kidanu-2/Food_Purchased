charge_food=float(input('Please enter the charge for the food : '))
tip_amount=(charge_food*18/100) # Tip amount in %
sales_tax=(charge_food*7/100) # sales tax amount in %
Grand_total=(charge_food + tip_amount + sales_tax) #display the charge of the food plus tip and sales tax.
print('Tip in $ = ',tip_amount)
print('Sales tax  in $ =',sales_tax)
print('The total_price in $= ', Grand_total)
