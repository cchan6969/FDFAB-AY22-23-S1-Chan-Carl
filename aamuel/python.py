'''
bill= float(input('Enter the amount spend: '))
member= input('Member? ')
if member == 'true':
    discount= 0.1
else: 
    discount = 0.02
bill = bill * (1 - discount)
print(f'Your total bill is', bill)
'''

k=(input('Enter a number to calculate its factorial: '))

def factorial(k):
    for i in range(k):
        k=i*k
        return k
print(f'The factorial is', k)
