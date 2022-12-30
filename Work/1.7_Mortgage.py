# mortgage.py
'''
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s 
Mortgage, Stock Investment, and Bitcoin trading corporation. 
The interest rate is 5% and the monthly payment is $2684.11.
'''
# Exercise 1.7
principal=500000
rate=0.05
payment=2684.11
amount_paid=0
month=0

extra_payment_start_month=61
extra_payment_end_month=108
extra_money=1000
while(principal>0):
    month+=1
    if(month>=extra_payment_start_month and month<=extra_payment_end_month):
        principal=principal*(1+rate/12)-payment-extra_money
        amount_paid+=payment+extra_money
    else:
        principal=principal*(1+rate/12)-payment
        amount_paid+=payment
    print(month, amount_paid, principal)


print('Total Paid ',amount_paid)
print("Months", month)  

