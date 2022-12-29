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
extra_money=0
while(principal>0):
    month+=1
    extra_money=0
    principal=principal*(1+rate/12)-payment
    if(month<=12):
        principal-=1000
        extra_money=1000
    amount_paid+=payment+extra_money
    
print(round(amount_paid,2),month," months")
