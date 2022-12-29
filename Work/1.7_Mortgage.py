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
while(principal>0):
    principal=principal*(1+rate/12)-payment
    amount_paid+=payment
print(amount_paid)
